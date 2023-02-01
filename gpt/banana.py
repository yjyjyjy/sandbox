import openai as ai
from pymongo import MongoClient
import pandas as pd
import time
import subprocess
import ffmpeg
from dotenv import load_dotenv

load_dotenv()
import os
import asyncio

from io import BytesIO
import base64
import banana_dev as banana


def getTranscript(fileName):
    with open(f"loadingDock/{fileName}", "rb") as file:
        mp3bytes = BytesIO(file.read())
    mp3 = base64.b64encode(mp3bytes.getvalue()).decode("ISO-8859-1")
    model_payload = {"mp3BytesString": mp3}
    out = banana.run(os.getenv("BANANA_API_KEY"), os.getenv("BANANA_MODEL_KEY"), model_payload)
    print(out)
    print(type(out["modelOutputs"]))
    return out["modelOutputs"]


# tsc = asyncio.get_event_loop().run_until_complete(getTranscript("sample.mp3"))
# tsc = asyncio.run(getTranscript("sample.mp3"))
tsc = getTranscript("sample.mp3")
print(tsc)
