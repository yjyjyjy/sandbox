import openai as ai
from pymongo import MongoClient

import time
import subprocess
import ffmpeg
from dotenv import load_dotenv

load_dotenv()
import os
import copy


# >>>>>>>>> Get Slicer <<<<<<<<<<<<
def get_database():

    # Provide the mongodb atlas url to connect python to mongodb using pymongo
    # CONNECTION_STRING = "mongodb+srv://user:pass@cluster.mongodb.net/myFirstDatabase"
    CONNECTION_STRING = "mongodb+srv://dev:36yqiFfvnWN5kwO2@cluster0.0kvcr5k.mongodb.net/?retryWrites=true&w=majority"

    # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
    client = MongoClient(CONNECTION_STRING)

    # Create the database for our example (we will use the same database throughout the tutorial
    return client["rina"]


from dotenv import load_dotenv

load_dotenv()
import os
import openai

openai.api_key = os.getenv("OPEN_AI_API_KEY")
from openai.embeddings_utils import get_embedding, cosine_similarity
import pandas as pd
from PyPDF2 import PdfReader

PATH = "resumes"


def extract_resume_text(filename):
    reader = PdfReader(PATH + "/" + filename)
    text = ""
    for p in reader.pages:
        pageText = p.extract_text()
        text += pageText
    return text


def get_embedding(text, model="text-embedding-ada-002"):
    text = text.replace("\n", " ")
    return openai.Embedding.create(input=[text], model=model)["data"][0]["embedding"]


resumeFileNames = os.listdir(PATH)
dataList = []
for filename in resumeFileNames:
    text = extract_resume_text(filename)
    dataList.append({"name": filename, "resume": text})
df = pd.DataFrame(dataList)

df["ada_embedding"] = df.resume.apply(lambda x: get_embedding(x, model="text-embedding-ada-002"))
# df.to_csv('output/embedded_1k_reviews.csv', index=False)


jd = """
Cryptosat is looking for a senior software engineer to join us in developing blockchain applications based on the interaction between ground and satellite software. We are a small team in a well-funded, early-stage startup. This position provides ample opportunity for technical leadership, ownership, and cross-functional impact, with minimal oversight and a large degree of independence. The position can be remote.



Desired Qualifications

Must-Have:

Industry experience with either C++/Rust/Go or equivalent systems languages
Experience with development for Blockchains such as Bitcoin, Ethereum, etc.
Experience with developing smart contracts over one of the major chains
Working knowledge of Python.
Thrives in an ambiguous and uncertain environment.
Independent and self-directed. Able to operate with minimal guidance.


Plus:

BSc in computer science or related field
Familiarity with cryptography algorithms such as RSA, Diffie Helman, and Elliptic Curves cryptography.
Experience with Solidity
Working knowledge of Golang
"""


def search_resumes(df, jd, n=3, pprint=True):
    embedding = get_embedding(jd, model="text-embedding-ada-002")
    df["similarities"] = df.ada_embedding.apply(lambda x: cosine_similarity(x, embedding))
    res = df.sort_values("similarities", ascending=False).head(n)
    return res


res = search_resumes(df, jd=jd, n=10)


meetingId = "6b90376f-43eb-49d7-9e0a-f774d02cbc8e"
dbname = get_database()
templates = dbname["templates"]
meetings = dbname["meetings"]

item_details = meetings.find({"_id": meetingId})
items_df = pd.DataFrame(item_details)
tranArr = items_df.iloc[0].transcripts
slicerDf = pd.DataFrame(tranArr).sort_values(by="timestamp")
# slicerDf.user = slicerDf.user.apply(lambda x: 'Scarlett' if x == 'Speaker 2' else "Abiodun")
slicerDf.timestamp = slicerDf.timestamp.apply(lambda x: int(x - slicerDf.timestamp.iloc[0]))


def groomSlicer(slicerDf):  # assemble the transcripts
    aggFunc = {"transcript": lambda x: " ".join(x), "timestamp": "first", "user": "first"}
    sTemp = slicerDf.head(0)
    currentUser = slicerDf.user.iloc[0]
    pointer = 0
    for index, row in slicerDf.iterrows():
        user = row["user"]
        if user != currentUser:
            chunk = slicerDf[pointer:index]
            chunk = chunk.groupby(chunk["user"]).aggregate(aggFunc)
            sTemp = pd.concat([sTemp, chunk])
            currentUser = user
            pointer = index
    return sTemp.reset_index()[sTemp.columns]


sTemp = groomSlicer(slicerDf)
sTemp = sTemp[
    sTemp.transcript.apply(lambda x: len(x.split(" "))) > 3
]  # remove the very short ones (usually just making noises to show attention)
sTemp = sTemp.reset_index()[sTemp.columns]
slicer = groomSlicer(sTemp)

# >>>>>>>>> get mp3 <<<<<<<<<<<<
inFile = "/Users/junyuyang/Downloads/38a56c1e-cec4-467f-8725-0b793972d83e.webm"
subprocess.run(f"ffmpeg -i {inFile} recording.mp3", shell=True)


# >>>>>>>>> slice mp3 into slices <<<<<<<<<<<<


def get_length(input_video):
    result = subprocess.run(
        [
            "ffprobe",
            "-v",
            "error",
            "-show_entries",
            "format=duration",
            "-of",
            "default=noprint_wrappers=1:nokey=1",
            input_video,
        ],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )
    return float(result.stdout)


length = get_length("loadingDock/recording.mp3")

## needs a bit shift which is weird
# slicer.timestamp = slicer.timestamp-50
# slicer.timestamp.iloc[0]= 0

for i in range(slicer.shape[0] - 1):
    start = slicer.timestamp.iloc[i] * 1.0 / 1000
    end = slicer.timestamp.iloc[i + 1] * 1.0 / 1000
    duration = end - start
    command = f"ffmpeg -ss {start} -i loadingDock/recording.mp3 -t {duration} -c copy loadingDock/slice{i}.mp3"
    subprocess.run(command, shell=True)

command = f"ffmpeg -ss {slicer.timestamp.iloc[slicer.shape[0]-1]*1.0/1000} -to {length} -i loadingDock/recording.mp3 -c copy loadingDock/slice{slicer.shape[0]-1}.mp3"
subprocess.run(command, shell=True)


# >>>>>>>>> get transcripts of each slice <<<<<<<<<<<<
from io import BytesIO
import base64
import banana_dev as banana

# Expects an mp3 file named test.mp3 in directory
def getTranscript(fileName):
    with open(f"{fileName}", "rb") as file:
        mp3bytes = BytesIO(file.read())
    mp3 = base64.b64encode(mp3bytes.getvalue()).decode("ISO-8859-1")
    model_payload = {"mp3BytesString": mp3}
    out = banana.run(os.getenv("BANANA_API_KEY"), os.getenv("BANANA_MODEL_KEY"), model_payload)
    return out["modelOutputs"]


transcripts = copy.deepcopy(slicer[["user", "timestamp", "transcript"]])
for idx, row in slicer.iterrows():
    print(idx)
    tsc = getTranscript(f"loadingDock/slice{idx}.mp3")
    transcripts.transcript.iloc[idx] = tsc

transcripts.transcript = transcripts.transcript.apply(lambda x: x[0]["text"])

meetings.update_one({"_id": meetingId}, {"$set": {"whisper": transcripts.to_dict("records")}})


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

filename = "/Users/junyuyang/Downloads/transcript.txt"
with open(filename, "r") as f:
    data = f.read().replace("\n", ",").replace(",,", "\n")

data.split("\n")

raw = data.replace("\n", "")
line = ""
arr = []
i = 0
for c in raw:
    if c == "[":
        if line != "":
            arr += [line]
        line = c
    else:
        line += c
arr += [line]


def convert_ts_to_ms(ts):
    arr = [int(float(e) * 1000) for e in ts.split(":")]
    if len(arr) == 3:
        return arr[0] * 3600 + arr[1] * 60 + arr[2]
    return arr[0] * 60 + arr[1]


def splitting(line):
    tsString = line.split("]")[0]
    start = convert_ts_to_ms(tsString.split(" --> ")[0].replace("[", ""))
    end = convert_ts_to_ms(tsString.split(" --> ")[1])
    tsc = line.split("]")[1].strip()
    return [start, end, tsc]


df = pd.DataFrame([splitting(line) for line in arr], columns=["start", "end", "tsc"])


def generate_gpt3_response(user_text, print_output=False):
    """
    Query OpenAI GPT-3 for the specific key and get back a response
    :type user_text: str the user's text to query for
    :type print_output: boolean whether or not to print the raw output JSON
    """
    completions = ai.Completion.create(
        engine="text-davinci-003",  # Determines the quality, speed, and cost.
        temperature=0.5,  # Level of creativity in the response
        prompt=user_text,  # What the user typed in
        max_tokens=20,  # Maximum tokens in the prompt AND response
        n=1,  # The number of completions to generate
        stop=None,  # An optional setting to control response generation
    )

    # Displaying the output can be helpful if things go wrong
    if print_output:
        print(completions)

    # Return the first choice's text
    return completions.choices[0].text


# resp = generate_gpt3_response(
#     user_text="""
# tell me a joke
# """,
#     print_output=False,
# )

# print(resp)
