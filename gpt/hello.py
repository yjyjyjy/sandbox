import openai as ai
from pymongo import MongoClient
import pandas as pd
import time


def get_database():

    # Provide the mongodb atlas url to connect python to mongodb using pymongo
    # CONNECTION_STRING = "mongodb+srv://user:pass@cluster.mongodb.net/myFirstDatabase"
    CONNECTION_STRING = "mongodb+srv://dev:36yqiFfvnWN5kwO2@cluster0.0kvcr5k.mongodb.net/?retryWrites=true&w=majority"

    # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
    client = MongoClient(CONNECTION_STRING)

    # Create the database for our example (we will use the same database throughout the tutorial
    return client["rina"]


ai.api_key = "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"


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

dbname = get_database()
templates = dbname["templates"]
meetings = dbname["meetings"]

item_details = meetings.find({"userId": "google-oauth2|108486050572122081728"})
items_df = pd.DataFrame(item_details)
tran = items_df.iloc[1].transcripts
scarlett = [t for t in tran if t["user"] == "Speaker 2"]
lines = [str(int(t["timestamp"])) + ":\n" + t["transcript"] for t in scarlett]
text = "\n\n".join(lines)
print(text)

resp = generate_gpt3_response(
    user_text="""
Below is the transcripts with timestamp in epoch format ending in ":".

Transcripts:

${text}

Below are potential topics discussed, separated by ">>":
>> What do you hope to get out of your business school experience, and why is Haas the right school to help you achieve this?
>> At Berkeley Haas we strive to develop equity fluent leaders who value different identities and lived experiences. How will you engage in and cultivate diversity, equity, and inclusion at Haas?
(If needed, probe: what experiences do you bring, {workplace, community orgs, etc.} that inform your interest in engaging in diversity, equity, and inclusion?)
>> Tell me about a time when you were in a heated workplace argument or debate in which you were ultimately proven incorrect. How did this make you feel? How did you react?
>> Tell me about a time when you led a project that was particularly stressful or complicated and team morale was low. How did you foster collaboration and what was the outcome?
>> Is there anything else you would like to share that hasn’t already been covered today?

Question: What is the timestamp of each of the topics? If you cannot find it, mark it as unavailable
Answer:
"""
)
print(resp)



Speaker 1 (0:0)
Hello.

Speaker 2 (0:1)
Hey, can you hear me?

Speaker 1 (0:3)
Yes, I can.

Speaker 2 (0:4)
Right, awesome.

Speaker 1 (0:4)
Hi

Speaker 2 (0:5)
Nice to meet you.

Speaker 1 (0:7)
nice to meet you.

Speaker 2 (0:8)
And how do I, how do I pronounce your name? Exercise.

Speaker 1 (0:14)
Well, the side of the world is called, I'm called Abiodun.

Speaker 2 (0:20)
Not abuse a building. Sorry, awesome, great. So um well again, nice to meet you. And thanks, thanks for taking the time today and, you know, congrats that, you know, you're getting to this round of the interview, it has. So we we have about 45 minutes today. So just wanted to, you know, walk you through the process. So I guess, first of all, it's sort of required by the school that I need to verify your ID.

Speaker 1 (0:52)
Yeah, I got an email as regards. That's I have my international possible here.

Speaker 2 (0:57)
Okay.

Speaker 1 (1:2)
Leave the lights.

Speaker 2 (1:4)
Yeah, yeah.

Speaker 1 (1:4)
Thank you.

Speaker 2 (1:5)
All good. Yeah, yes and Awesome. So yeah, just the admin the, the housekeeping stuff so I, you know, I do have you sort of a list of mandatory questions that I need to go through with you. And then obviously, I wanted to save

Speaker 1 (1:20)
Okay.

Speaker 2 (1:22)
some time towards the end. You know, in case you have any questions or, you know, if you're sort of debating between schools. I'm hoping that I can give you some perspective. So, I graduated from Haas, back in 20 17. So it's been A more than five five years.

Speaker 1 (1:40)
I guess, yeah.

Speaker 2 (1:42)
That's why. Yeah, we just had a, we just had our

Speaker 1 (1:42)
Well.

Speaker 2 (1:44)
five five year reunion last year, you know, time had a pretty, pretty

Speaker 1 (1:47)
That's great.

Speaker 2 (1:49)
quickly. Yeah. So, you know, any any questions you might have about, you know, has about, you know, culture people career, you know, we can save it for for, you know, for the last piece of today.

Speaker 1 (2:1)
That's great. That's great.

Speaker 2 (2:2)
And okay great. So you know first question or do you hope to get out of your business school experience? And why is house to ride school to help you achieve this?

Speaker 1 (2:15)
All right. Thank you. Thank you. Foxing that question. So, One of the things that I've been looking forward to in business school, is actually to expand my knowledge in the business setting, you know? So currently I work in a health, technology startup and I've transitioned for my career from garlic intent, to business development, executive and currently. Now, I'm working as the public sector lead whereby. I manage the projects that the company has with the government and For me, it's practical knowledge, you know, learning on the field interacting with these people, you know, being exposed to, you know the government set and how they do their work, you know how they how the healthcare system works in terms of the public sector, you know. So I'm hoping that you know. Well I want I want to come to us to learn more of the theoretical knowledge and how I can, you know expand more on what I really have, you know, in my own what I do currently and then gain that business knowledge from us whereby They have the curriculum is one of the things that attracted me to the cost the for instance, innovations in healthcare. I mean, when I saw that part of the curriculum, it was something that really inspired me to, you know, put my application in for us, you know, because I believe that when you're exposed to those kind of courses and, you know, I have experienced people coming to teach you to train your own, how to, you know, do things in a moment methodological way, you know, it's also builds on that knowledge that I already have. So that is majorly. You know why I am, you know, applying to us. And I'm and I believe that, you know, having that experience is something that I know that, yes, it's going to help me, you know, build my business knowledge expose me to, you know, the practical cases in the United States. the United

Speaker 2 (4:22)
What, you know, I guess that the second half of the question was, What

Speaker 1 (4:26)
Yes, second question.

Speaker 2 (4:26)
why do you Why do you think has is the right school? To help you.

Speaker 1 (4:30)
Yeah. Well, like I mentioned before I wanted to, I've always wanted to build more on my business knowledge. However, one of the things that really attracted me to has was the ability to earn two degrees, you know, simultaneously like combining body mph and MD together, you know? And when I saw the the curriculum of the, the thoughtfulness and how to, you know, you in what they have done to put this thing together, you know, it was really something that I was I was amazed and I thought you know going for this was going to be like a good opportunity for me, you know? And then also the The location. I mean, it's it's one of I would say one of the top, you know, on the top places where it's when when it comes to technology, when you want to learn more about advancements in, you know, in technology these are places that, you know, it's that gets more attention, you know. So I believe that has is going to, you know, give me that experience. Give me that exposure, you know, to this kind of And reality, you know, the reality of things in a developed nation, you know, as compared to where I am currently, you know? So it's more it's more on learning, more exposing myself more from what I'm doing. Currently, in my own development and developing country as to what is happening in, you know, in the United States.

Speaker 2 (6:5)
Thanks for sharing. And the second question is, so at Berkeley House, we strive to develop equity fluent leaders who value different identities and lived experiences. How will you engage in and cultivate diversity equity, and inclusion at Haas?

Speaker 1 (6:28)
And thank you for that question. Okay? So, When I was doing my research about us, I you know, and and I attended some of the webinars. They made so much emphasis on the community, the community that I built and the technique community, you know? And I realized that it wasn't just something that it's not like they're picking students from, you know, one particular sector or one particular Country, you know, the, you know, posting it together because everybody's bringing different experiences. So I believe that my exposure in Africa, in Nigeria, you know, is some of the things that I, that would be very valuable for the House community. You know, I have been for years now. I've been very committed to healthcare healthcare development, you know, and those are the kind of things. I feel I would bring to the Healthcare Association. Has health care association and also

Speaker 2 (7:26)
No.

Speaker 1 (7:27)
even learn learn the role of women in the Women leadership club, you know? So those are the kind of places. I feel that I have something to share. I have something to contribute to the community and also learn from my peers as well.

Speaker 2 (7:43)
Hmm. Do you have any sort of more sort of specific? Let's say, You know, experiences, for example, you know what, what kind of, you know, experiences in along those lines that you will bring? And, you know, either it's from the workforce or the community that you're currently serving, that would,

Speaker 1 (8:1)
Okay.

Speaker 2 (8:3)
you know, inform your interest

Speaker 1 (8:3)
Thank you.

Speaker 2 (8:4)
engaging in the overall diversity, equity and inclusion.

Speaker 1 (8:9)
Oh okay. All right so for instance currently I'm working as the public sector lead of the healthcare startup and we have a project that we're running. Now this project is focused on digitizing primary health care centers in Lagos states. Now the Project School covers 20 local government areas in the United States and we engage the healthcare workers, the, the administrative workers. You know, Health Care Workers, Ranger from the doctors to the nurses, to the Community Healthcare extension workers, you know, to the lab technicians that the pharmacist as well, you know? So, having youth that relationship that connection with the healthcare's primary health care system in Nigeria. Here is something I feel it's very valuable for the past community

Speaker 2 (9:6)
Hmm.

Speaker 1 (9:6)
something that I will bring you know, to the To for them to also learn from where I'm coming from because digitizing primary health care centers. It wasn't really it's not, I would say for my experience so far, it's it's not an easy process, you know? Because for a very long time, they have been using the traditional method which is writing with paper and pen, you know, but then we're coming in to say, Okay, start using devices that using technology and this is something that the change process has been very difficult, you know, because there's a lot of persuasion even negotiation, you know, to make sure that they keep on using and the consistently used. So it's not just that. Yeah, you know, using one thing and they're dropping one thing, you know, so it's pushing them that change process has been very difficult and and that I said, as my professional experience. So one of the, the leadership community that I joined was Young African Leaders Initiative and this program was, it's Sponsored by the United States. Uniseaid sorry, USA, ID search trying to remove, so it's sponsored by them. And these, the way they structure, the program is not focused just on Nigeria. We have person, and participants from Ghana, we have had spent from Uganda. You know, we have the, a lot of people from different African countries, apply for this program. And I was one of the people that I was selected for it. You know, and in during that program, I learned a lot about about Africa. You know, about not just, you know, Nigeria. But learning from people from Ghana and, you know, and my specialization attract, well, when you apply you have to pick you, specialization track and mine was public policy and management. You know, so I learned a lot from people from outside my country where they talk about the the situations, the the real life challenges that they are facing. And the program helped us to also become good lead. Become good advocators. So those are like the experiences that I felt that, you know, I've experienced diversity from And I feel that I would bring that to the House community.

Speaker 2 (11:30)
Awesome. Great story.

Speaker 1 (11:32)
Thank you.

Speaker 2 (11:33)
The next one. Is let's say. so, tell me about time and when you were in a heated, workplace, argument or debate In which you are ultimately, proven incorrect. How did this make you feel? How did you react?

Speaker 1 (11:57)
Hmm, it's a very interesting question. okay, so I remember one time when we so when we started the project, In terms of structure. So the projects that I'm talking about, that's the Lagos State Primary Healthcare Digitization project we needed to I I function as a project manager and I needed to build a very good communication structure for my team, like I wanted something that would was going to be very effective and would something that I can easily respond to, you know. so, I wanted to use the the informal way which was using Whatsapp. I thought, If we're gonna have everybody that just have them everybody want, you know, together on on Whatsapp, you know, but then I spoke to my boss about it and he recommended that season. What's up is very informal for. So things like that is best, we look for a better way, but then I thought, People are used to water. Let's just use what like you know, I would have something that was going to be easy for people to use so that they won't. If I want to bring in a new communication strategy, it's going to be something that would be very, you know, very hard for for me to start teaching people. You know how to use this particular platform. So he recommended slack, you know, that I should use slack as a communication channel, but I hope we were not using that before then. So if I want to bring it now I'll have to like train people or even I myself will have to learn how to use slack, you know? So but then it was you, it wasn't so much of it because it was between me and my boss. It wasn't a heated argument. It was something that I really needed to sit down listen and learn from him, you know, to really understand why he was recommending that what we can that be can, can that be implemented? And, you know, if there's a need for us to watch, maybe YouTube videos on how to use slack because that was what we ended up doing, you know? Then so be it, you know? But then it was very important that I implemented a very effective communication channel and you know, with his support which is learning. You know, I was, I was able to just, you know, Why not give it a try? Because yeah we want to train health care workers on how to use technology.

Speaker 2 (14:17)
You know.

Speaker 1 (14:18)
You know how to use these talk solutions. Why wouldn't I also embrace using something, you know, something different?

Speaker 2 (14:24)
Yeah.

Speaker 1 (14:24)
Which I did. And that was the outcome.

Speaker 2 (14:28)
How did you how do you like using slack?

Speaker 1 (14:33)
Man, when I went through all that, when I started, I watched our YouTube video. They have a tutorial video on slot and on YouTube. Yeah. And when I watched it, I realized that you can just create one channel

Speaker 2 (14:49)
Huh.

Speaker 1 (14:50)
but you can just raise slack one login and then have multiple channels. And it was something that I thought it was easy because before what I wanted to do was to create different whatsapp groups. And there would not allow communication between things, you know, but then using slack was was a very easy route for me and I utilized I think every utilized almost all of their features you know locking some locking some channels depending on hierarchy you know and then you know having meetings and you can even make phone calls or slack. You know post videos I utilize a lot of features that he had and I realized that okay, that this was actually way much better than using Whatsapp gave me proper it.

Speaker 2 (15:36)
Yeah.

Speaker 1 (15:37)
Gave me a proper structure. I mean, a proper projects, you know, management structure when it comes to communication and I really loved it. I really loved. I do still love it. I still use it.

Speaker 2 (15:51)
Yes, that's life is pretty awesome.

Speaker 1 (15:52)
To use it. Yeah.

Speaker 2 (15:56)
All right, so the next one is and let's say, tell me about a time when you when you let a project that was particularly stressful or complicated. And a team morale was low. How did you foster the collaboration and what was the outcome?

Speaker 1 (16:17)
Okay. Very, very good question because it's really it's very well what I'm doing right now. So, when we started implementing the projects that the digitization of the primary care centers in Lagos state, when we started implementing it, we needed to hire a lot of people. So I reached out to the HR, you know, and then he, he did, you know what, he could do to bring in more people. Now, where digitizing 20 comprehensive centers. I mean, when I mean compressor, I'm talking about them centers where they are doing all healthy. Sorry about that. Yeah. Providing, you know, all healthcare services. Excluding of course, excluding secondary type of care. you know, so for for me it was like, okay I needed people and you know, and a lot of people I need to, you know,

Speaker 2 (17:13)
How many, how many, how many do you need?

Speaker 1 (17:16)
I was pushing for like 150, 150 people. I wanted like a minimum of like five per facilities because in one facility you have you can have like 20 to 30 healthcare workers. so, I needed like, I was, I was requesting for like five people like I want a lot of people I want this project to succeed and you know because it was something that I it was an opportunity for me you know and I didn't want it to feel. So I wanted to request for all the resources you know that I could get you know but then We got that number. We didn't get up to 150, of course. But we got a very high number about 1997 and we deployed it into the 20 healthcare centers. However, there were some that were leaving, you know, at some points because they didn't have to go back

Speaker 2 (18:10)
You know.

Speaker 1 (18:11)
to school, you know? And he was like, How can we manage this? How do we make sure that the project still continues in this facilities? So, you know, I restructured the team and I said, Okay, it's best. I make one person accountable for a facility. So I made sure that there's a, there's one representative in each facility and it reduced the number. You know, we had, we came out to less than 30 you know, to Also, I would say, because, of course, manpower planning. It was, it was quite a lot for us, you know? And so we reduced the, we reduce the number but, Right now, I would say it was a good, it was a good one because the project was in faces, when we started it, we needed to train, we needed to, you know, but now we're just making sure that they are using. So reducing the number wasn't so much of a bad thing was a good one, but then it's also gave this people the opportunity to be leaders in, you know, and be responsible. You know, be accountable for the success of the project in the facility.

Speaker 2 (19:30)
Right. And I guess, you know, how did you Address a little bit of these, you know, I know the turnover was high and how about the team around at the time?

Speaker 1 (19:42)
Well, the team world was still up because for me, I made sure that I was communicating with them every single day. I made sure that they are Being there are, they are professional doing their jobs, you know, they are not. Yeah. You know if If your facility succeeds and they use and the healthcare workers in that facility are using dissolution, it is your own success, you know. So I wanted that I wanted them to really take, you know, be proud of what they're doing. So I communicated with them every day. Still well till now, I still communicate with them everyday uses. Like, you know, and I made sure that they don't feel down at times. Of course, they do feel overwhelmed, you know, because they have to move from one unit to another unit or another unit which can be very, very hectic for them, you know? But then I make sure that the case I

Speaker 2 (20:40)
Hmm.

Speaker 1 (20:42)
walk, if you can, if you if you're able to succeed with one unit today, move to the next unit, probably the next or the, you know, all the week after. So it was very much important for me to communicate with them like every single day. And I made sure that this is this part of mind is not, I would not for me as well. I get tired, it's a lot of work, you know, but then I I know that the project success is the company

Speaker 2 (21:5)
Yeah.

Speaker 1 (21:9)
success and it's also my success. So You know, having that in mind and even when I get tired, you know, I always use that as my motivation that it has to succeed, it has to succeed. You know, and I also pass that, you know, that feeling to them that you know, if everything works, well, you're facility is your success, you know, so be happy and do whatever it takes to make sure that you know, everything works fine.

Speaker 2 (21:35)
For me, awesome. Thanks for the story. Thanks Let's say, Okay, let's go quick one and what is the most valuable piece of constructive feedback you have received? So far, your

Speaker 1 (21:52)
Hmm.

Speaker 2 (21:54)
Life or career.

Speaker 1 (21:57)
Okay.

Speaker 2 (21:58)
How did you obviously, how did you

Speaker 1 (21:58)
Ah, constructive feedback.

Speaker 2 (22:0)
react to it?

Speaker 1 (22:3)
Okay. Well. When I started doing the groundwork, let me just use my career. It's it's not recent it's really not

Speaker 2 (22:15)
Okay. Yeah.

Speaker 1 (22:18)
recent. It's I think it was 2021. That was when I was only one doing the groundwork. Now groundwork means that I was meeting the healthcare workers in those different places. Because of the company culture, you know, the company's culture. The way I work, you know, the way I do things, I want to maintain a type of lifestyle, like, a type of work pattern work, ethics, you know, to make sure that if I want, if you schedule a meeting with me at this time, then you should be done at that time, you know? So I had a meeting with one of the steel group stakeholders. and, you know, I'm getting there, you know, before the time of course, he was not available and I was, you know, I was I was angry because I already I had another meeting afterwards. My, my body language, you know, it all changed because I was like, Where is this person? He didn't call me, he didn't tell me that was gonna be available. It is anything. And so, I After like 30 minutes, I left the place. Like, if you're not gonna meet me then, you know, what's the point? I need the place and so my way out, I told my boss about it, you know, and then he said No that I should have done that. I was like what I was right? Like he's scheduled me to be at this time. Why do he, you know, tell me that he wasn't gonna be available. You know, I was trying to prove that yes, I had every justification you know, to leave the place I was trying to tell my boss that yes. We women treat at this time. She didn't meet her at this time. So if I'm gonna leave, then don't blame me. Like, you know, but then

Speaker 2 (24:4)
but,

Speaker 1 (24:7)
He was trying to correct me that. even though, you know, she didn't show up at least you would have called him, you would have dropped in the message, you know, he was well in my mind like, We fixed this time like but then, I just I was I remember very well. I was in the bus that day I was already. I really left. I was in transit. And while he was talking to me on the phone, I started feeling bad like Well, did I do anything bad? Like I was translated feel like I had every right to leave, you know? So then it really got to me like my boss correcting me. Telling me that you don't. If people don't show up. Give them the benefit of those don't don't be angry. You know, don't act like you know you had every right, you know. You have to be patients with these people. They're you know, you're trying to tell them about something that they haven't done before.

Speaker 2 (25:5)
Mm-hmm.

Speaker 1 (25:6)
You have to be you have to be very patient. You know that was that was the message. He was trying to pass to me, that's when you need to engage people that they are used to what they, you know, they do before and they don't want to change, you have to be very patient with them and teach them and help them, you know? So next time. So he corrected in the next time if he's not gonna be able and and you know, if he's not around you can just dropping me a message you know and then call him if he doesn't pick, you know that? Yes you made an attempt. To reach out before taking the action to me, you know. And so I Am on my way home Daddy. I just, I just caught the man and then, you know, he was like, Oh, he was sorry that he wasn't defeating and then his phone was switched off, and you soon was on silence, you know, and he was trying to like apologize. And then in my mind, I like cheese. All right, now, I don't have to, I don't need to be angry anymore. Let me just, let me just become

Speaker 2 (26:4)
Right. Right.

Speaker 1 (26:5)
really Yeah, so I just

Speaker 2 (26:6)
So you end up, you end up meeting that person.

Speaker 1 (26:11)
Yeah, I did. So we fixed, we fixed the next day. In fact, the next day we fixed for 9 am the next day and he will go to his place of work before me. Here, I was surprised like, because normally, you know, those kind of people because they are because of hierarchy. Yeah, the bosses, you know, Yeah, they might not show up on time and all of that, but then I, I got there like nine and like 8:50 And then here, you told me that I was there like it. And then we had an awesome discussion.

Speaker 2 (26:47)
And rice. Awesome. So you know, these are sort of all the mandatory I call them financial questions that I need to ask. But you know again there's this one last one if anything you know so I I don't have your essay so you know basically I don't you know I don't get the chance to read your essay but I do have a resume. So you know have that in your mind

Speaker 1 (27:11)
Okay.

Speaker 2 (27:15)
and is there anything else that you

Speaker 1 (27:16)
Okay.

Speaker 2 (27:17)
would like to share and that hasn't already been covered today?

Speaker 1 (27:24)
Well.

Speaker 2 (27:26)
Before we get to Q&a's.

Speaker 1 (27:29)
okay, well, I actually love to talk about. Probably my project in school. But then it's already it's already and it's already in my resume that I had and I have a publication. you know, but the experience for me was, It was. It was heavy for me at that time. I don't know if you'd like to hear about it.

Speaker 2 (27:55)
Yeah, you know, if you think it's, you know, you if you wanted to share and you think it's, you know, anything you want to share that, you

Speaker 1 (28:2)
Okay.

Speaker 2 (28:3)
think it wasn't.

Speaker 1 (28:4)
Okay.

Speaker 2 (28:4)
It wasn't being covered.

Speaker 1 (28:6)
Thank you. All right, so my final year or before my penultimate here, I I was assigned a project supervisor. And he specialized in near pharmacology. Sorry, never. Never pharmacology. Sorry. Specializing never pharmacology. And he wanted us to, you know, walk on and cancer drugs. In the effect of ANTICASSO drugs on the kidney. in other time, it was an exciting topic for me was something that I thought that, you know, I would really, you know, love to, you know,

Speaker 2 (28:48)
Hm.

Speaker 1 (28:48)
walk on

Speaker 2 (28:48)
M.

Speaker 1 (28:49)
But then the impact of the project of me was way beyond. Because when I was in research about About anti-cancer drugs in general. And I was seeing pictures. I was saying people that had cancer, you know, things like that. It's all, it's all I felt really. It's I thought it was that some point because I was wondering what exactly they. How, how people, how do people go through this health cases? And they are, you know, and they are sublisted to drugs, that would still have strong side effects on them, you know? And so I, you know, I started the project, you know, got vista rats, got my, got the drugs, the vitamin E. And then the the plant extract was miguela sativa, which is a black seed. And, you know, the extraction used ethanol to do extraction, you know? And then Conducted the actual experiments to, we go to the results, you know. And so for me the the cost, the experience it was it was something was something huge for me because I wasn't really at the time, you know? I didn't know what. Life could be for somebody, you know, battling with things like this. But then my supervisor saw my work and thought that, okay, I did something like I he was it was it was a good project. It was a very, very good project for me and and then I think the year after, you know, we recommended it for a publication, I was I was really happy about that, you know, I was really, really happy. I just wanted to talk about it because for me, wasn't. It's not, it's not so normal here in Nigeria, you know, where you get to do certain work and then you get a publication after, you know, it's something that lecturers would have to scrutinize and scrutinize. I want to see if you are worthy of the publication or not, you know? And so And so And so yeah, it was it was a very good experience for me. I just wanted to like talk about it and and then share how my my love or my blessed, my vibe for healthcare development. How do how everything was built up? You know, haven't seen that and then outside that my my niece also go and meet it. and the hospital, you know, and it was a very trying time for my my sister because, The experience that she had was a very, I wouldn't, I won't say terrible. Terrible, terrible, my sound to watch, but it was terrible. It was, you know, because the healthcare the nurses were not doing their own parts. They were not educating that they were not sitting her down. It's okay, this is what we're trying to do. We haven't got any diagnosis but we're trying to, They were not doing that. This was they were just living on saying, Oh, go under the distance. And when she called me, you know, she was worried, she was scared like like Why, why is that nobody's telling me anything? Why am I just going out to do tests? You know? And so all this experiences are things that really built up my health. You know, my my love for healthcare development. I mean it's a different thing when you are just when you just learning it in classes, when you have your own experiences, when you have, you know, things that you can really that would really get to you. Then it's it's a different thing entirely you know. So I just wanted to talk, you know, build more on why my my love for healthcare development has Has been like you need to go for me, You know, a major goal.

Speaker 2 (32:54)
Yeah, no. This is awesome. Yeah, and I know you know, I wasn't coming from the MPH program but I you know, know a lot of people from there, you know. It's it's a very it's a relatively small community, you know, compared to, you know, the the overall MBA program. But I think, you know, people are amazing and everyone has sort of a very, very strong passion and love for for healthcare. And I think most of them, you know, At least the people that I still in contact with, you know, my year or the year above me or year and they're me, they're so in the healthcare space. So, you know, I think this is a sort of very small, but very tight community that everyone, you know, share the same sort of passion towards towards health care. Thanks for for sharing, great. So yeah, awesome. So, these are all the questions that I have for you. You know, we have roughly in a 10 minutes left. So I wanted to, you know, open it up and and see if you have any questions or if about Haas about anything or, you know, about, you know, my experience or if you need additional information about, you know, us anything

Speaker 1 (34:5)
Yeah, thank you. So I when I got my email for the invitation for interview, Of course, I was really happy because they're okay. My application makes us to be admissions community

Speaker 2 (34:19)
Yeah.

Speaker 1 (34:21)
Yeah. So And then your name was in the was an email which I went to check you on LinkedIn. Apologies, if he looks like stalking, you know what?

Speaker 2 (34:32)
No, no, no.

Speaker 1 (34:35)
Yeah. Yeah, I went to check you on LinkedIn to see if there was if there was a correlation you know but then I saw that you're in the Fintech space. Which is a very booming it's a very booming space right here.

Speaker 2 (34:52)
Hmm.

Speaker 1 (34:52)
In Nigeria, I mean fintechs are like the magnets, so like that was doing the thing.

Speaker 2 (34:58)
Yeah. Yeah.

Speaker 1 (35:0)
I don't do in the big thing here. So I really wanted to know how how is it a way that Fintech and he'll take Can you know merge if there is if you have an experience in that or maybe you have, you know, probably there's something that you feel fainted has that can be brought into the healthcare and health tech space, you know, as well. Yeah, that's my first question.

Speaker 2 (35:27)
Yeah sure. And so you know do you want to finish

Speaker 1 (35:30)
Okay.

Speaker 2 (35:30)
your question first? Or do you want to do? You want answer first?

Speaker 1 (35:33)
Okay.

Speaker 2 (35:34)
Okay.

Speaker 1 (35:35)
Okay.

Speaker 2 (35:37)
Great. So, you know, I guess just from coming from my perspective and based on what I saw here, you know, obviously I can't speak to sort of other countries or other market but overall there has been quite a few so we're strong application between sort of healthcare over a healthcare space and fintech I can give you a few examples, you know. You know, the overall sort of medical bill is pretty crazy here in in a state, right? Like if you don't have any insurance and obviously not everything is covered by insurance and and you know, how do you help people sort of making payment is one problem? Or, you know, question that people trying to solve for and then especially some of them are in the, you know, even a woman. If it's, you know, Fertility space, for example, right? Like, say You know, a lot of people in my age is considering, you know, for example, doing like IVF. You know.

Speaker 1 (36:43)
Yeah.

Speaker 2 (36:44)
And a lot of those things aren't covered by insurance. So you know what what Fintech brings

Speaker 1 (36:48)
Yeah.

Speaker 2 (36:49)
in is some sort of sort of lending like solution where you know, for example, For a woman. Obviously when you're you're younger. Well, if if you're considering let's say, you know, you're considering doing it IVF, right? You probably wanted to do it while you're younger, but you, you don't really have that much money, but when you end up, you know, when you're making progress your own career, you are are making more money. But then, you know, it's probably too late for you to consider that as an option. So there there's a, there's a mismatch there, right? For example. So how do you, how do you take that into account? How do you, how do you Let's say assess someone's profile, based on when they're 25 or 28. And and give them a loan, right? To to make sure that they have that option, ready for them before they were 20, but they're 30. But also at the same time they can pursue your career and eventually you're you're looking for a loan to be paid back, right? But I think it's a it's a very sort of strong. Need for the, for the women to have the option at the time, instead of like, right? Like when I'm when someone was 28 20 25, they probably don't have the financing that's required or needed to as an example.

Speaker 1 (38:9)
Yeah.

Speaker 2 (38:11)
There are all the other options for example, like, If we go to dentist office, right? If you want to do something, but it's, you know, too expensive at the, at the point, How do you know plug in a fintech solution right there and be like, well, based on your profile thinking, You know, access your profile in? You know, I said in seconds and yeah, based on profile and give you a installment. And so that, you know, you don't have to worry about that today. It's basically alone, but it's easier. Like, you don't have to go to the bank, right? It's more. Like How do you facilitate these conversations or help these, you know, healthcare providers to provide services to more people and, you know, obviously not, you know, we're not talking. About, you know, giving those solutions to like random people without any sort of assessment.

Speaker 1 (39:1)
Yeah.

Speaker 2 (39:1)
It's more like if you really need them but you know, you but you can't afford them today. How do you make sure that there's an option for them? And you know, honestly at the end of the day it's it's a win-win situation, right? The healthcare providers, whoever is the service providers are making more income revenue. Right? They they have access to more users

Speaker 1 (39:22)
Yeah.

Speaker 2 (39:23)
but on the user and the customer side, they they now have the option to to, you know, to to get the the, you know, the services that probably not available for them before as an example.

Speaker 1 (39:40)
No, that's that's great. You know, the reason why I access that here in Nigeria, we, you know, everybody's just acting on their own sector. So fintech I just, you know, doing that thing. He'll take also doing that thing too. Finding that right balance where boots because what isn't, you know, utilizing technology. So if there is a way we can actually make things work together And then, you know, people can actually access care.

Speaker 2 (40:9)
Hmm.

Speaker 1 (40:10)
You know, it's I feel it's very important because Everybody's going to not. Well, might not every might not be everybody, but then there's gonna be one time that one we need to access care, you know, at some points, and it's always important way by patients that, you know, they have access to money. Or like you said, lending opportunities, you know, for them to

Speaker 2 (40:31)
Yeah.

Speaker 1 (40:32)
also have access to. Okay. Thank you for explaining that. And lastly, I wanted to know about your house experience. I mean, I For me I haven't what I have. Lived it I've left Nigeria I've been to I've been to Ghana and I've been to Dubai. Those are like two countries that I have you know gone to outside mine. but, and we're just, you know, trying to think or imagine, you know, explore imagination. How would my experience? It has been like, the people, the, the school, you know, just how was your experience like

Speaker 2 (41:15)
Yeah, overall obviously it's amazing. Overall And, you know, if you're, if you're coming from, you know, another country, I could guarantee you that, you know, it's just that there are people from probably 30 40 countries in in one class so you can find people coming from different background, different community and pretty easily. And not just the people in your year. You know you also have access to the people and you know you're ahead of you right. Right. When you're a year one there there's another sort of class of year too in school. And when you're year too there's another sort of class of students that you know that just came. So you know, you basically have access to not just your year, but the year both ahead and and after you

Speaker 1 (42:6)
Well, okay. Okay.

Speaker 2 (42:9)
And, and, you know, I'll set of classes. You know, obviously I'm talking about experiences as a past classes is probably the relative to the boring part. And, you know, you have all these different clubs, right clubs communities that you can you can have access to and you have all these you know, travels. I would say one of my highlight was definitely travels. You have you know, spring break winter break? And you know summer you chances are you you need to do some sort of summer internships or probably you don't have that much of a, you know,

Speaker 1 (42:39)
Yeah.

Speaker 2 (42:41)
vacation. But you know before I think before summer before your summer internship, there's sort of a month in in May and June, where you also came travel if you want or there are some projects you can work on. And yeah for me I think the biggest highlight was definitely the travel piece because, you know, there are there are all these different tracks where, you know, they're organized by people. Coming from from that country. For example, I think one of the One of the biggest track one of the most popular track at Haas at the time. I don't know if that's the case for today. I would imagine it might still be which is the the Japan track. Like every year, you know, people you know you always have classmates from Japan. So they will it's almost like a, You know, they inherit that from from people ahead, you know, you know, a year before them and it's it's almost

Speaker 1 (43:36)
Previously.

Speaker 2 (43:36)
like a program and they would, you know, basically put together a a trip and you sign up for it and it's usually like Super, Super popular. Like we're talking about like 50, 60 people going to Japan like together.

Speaker 1 (43:50)
Well.

Speaker 2 (43:51)
Yeah, it's, it's probably one of the most popular track and you get the best and most authentic experience, right? I personally didn't go to that one, but I went to a track to Peru. Which is, which was also organized by

Speaker 1 (44:7)
Oh wow.

Speaker 2 (44:8)
my classmates who came from Peru and we had, you know, 40 45, people altogether, like it's just those things. These access you would never be able to get access to or not. Never. But like it's very hard for you to get access to. If you're just, you know, a normal tourist, right? You just don't have the access.

Speaker 1 (44:27)
Yeah.

Speaker 2 (44:29)
I think there's another one, which is pretty. Exclusive. That's the, the The one went to went to Israel.

Speaker 1 (44:41)
Okay.

Speaker 2 (44:41)
and another one is sort of they they sort of some some of them organize some local like some meetings with some like High up people in Israel like talking about, you know, the the tech community there, which is, you know, basically pretty pretty amazing. So I think personally that's that's the biggest highlight for me and obviously there are all these other activities. We're like, Oh these Holidays. There is a bar of we call them Bar of the Week. every Thursday, so Friday is

Speaker 1 (45:10)
Okay.

Speaker 2 (45:13)
Friday has no class. And probably only has, you know, these these sessions where, you know, if you want to have, if you have questions for the TAs, that's what, you know, when you go. But, like Friday doesn't, there's no class like Thursday night is probably, you know, the the weekend the night before the

Speaker 1 (45:30)
oh,

Speaker 2 (45:30)
week. So, it

Speaker 1 (45:31)
thank you.

Speaker 2 (45:32)
so it's, you know, bar of the week, you know, they pick a bar near campus and, you know, people just go

Speaker 1 (45:43)
Well, okay, I'm really looking forward.

Speaker 2 (45:46)
Um, yeah.

Speaker 1 (45:46)
To having that experience.

Speaker 2 (45:49)
Awesome.

Speaker 1 (45:49)
yeah, just see beyond

Speaker 2 (45:50)
Any, any other? Yeah.

Speaker 1 (45:53)
well sorry.

Speaker 2 (45:53)
Anyway,

Speaker 1 (45:55)
Well last one.

Speaker 2 (45:55)
Yeah, sure. Sure.

Speaker 1 (45:57)
alright, so So, Yeah, I was also going through on the career paths in, you know, helped on the escalator parts, we career as little pathway. And yeah, I found that digital health was one of its SO that really excited me, you know, but then I'm also thinking of what about Out like outside school. Like when you're doing school, like Were you able to like utilize some of your networks to get a job? Like You know those kind of things like walk you know getting a job outside school Like Was it easy Was it something that you had to you know, plug into some networks to you know to do that, You know? So because for me of course it's like I don't have, I've just gonna build my own network there, you know? So I just wanted to know like, what's really like, you know, getting a job outside. It's like, after finishing from us,

Speaker 2 (46:57)
yeah, so um, I always say there are two two different Paths. And if you're considering, let's say if you're considering joining a large company, Where, you know, by saying large, it's like, you know, they they have sort of existing relationships with the school career management office, right? So that's a, that's a pretty pretty big group at Haas and they're pretty resourceful, but I would say given the nature of it, they cover those big companies pretty well meaning, you know, companies have You know, Programs they come to campus on campus, or at off-campus recordings every year, you know.

Speaker 1 (47:40)
Okay.

Speaker 2 (47:42)
I, you know, rest assured, you know, has does have those access and you have, you know, you definitely have these, you know, access to information any specialty, if they come to campus to to hire people every year, chances are you're gonna have some alum. You know, some people graduate before me, that's already working at those companies. So you can have, you know, conversations, you know, go relationships, build network from there. So, that's one. And so considering, if you're considering joining a big company and chances are there covered by the

Speaker 1 (48:16)
Okay.

Speaker 2 (48:17)
career center, There's another pass which is, you know, pretty. I would say another big one here which is the startup route.

Speaker 1 (49:6)
Well, so sorry.

Speaker 2 (49:6)
Hey.

Speaker 1 (49:7)
But yeah, my network just went over.

Speaker 2 (49:10)
Okay. All right, I don't think I can see you but you can't hear me.

Speaker 1 (49:19)
Yeah, I can hear.

Speaker 2 (49:20)
Yeah.

Speaker 1 (49:20)
Oh sorry.

Speaker 2 (49:21)
All right, yeah notice. Um, where was I? Oh, there's another path which is also pretty popular. That's the the startup pass where you know there you know you're in Silicon Valley. Right. There are so many startups out there. There is healthcare startups. And all the other ones that you you might, you know, be interested in too. And it's very hard given the number of that, it's very hard for the school to to connect you to those companies because, you know, there's too many of them and they're right,

Speaker 1 (49:52)
Okay.

Speaker 2 (49:52)
very small. So if you're, if you want to go through that past because you know, some people are like, there's no way I don't want to join a big company, it's just not me some of them. Like I only wanted to go to start up if you wanted to go to that route, I would say You are most likely on your own to build some of these network. It's just a nature of it, right? Like they're they're small and chances are they don't have, They don't have structured programs right in terms of like hiring. So you really need to just go out and

Speaker 1 (50:22)
And thank you.

Speaker 2 (50:24)
and pitch for basically, you know, build relationship, build network and pitch yourself, right? And into into that. And and also timing way. Is this also very tricky because You know, for the for the big companies, they can come to campus in January and be like, Well, I need some interns in June and it's fine because, you know, they run this structure program every year, but it's very hard for startup to predict that they need people in January and

Speaker 1 (50:55)
Thank you.

Speaker 2 (50:55)
they're like, Oh, like, I don't know. Like maybe, you know, come back and talk to me in April. I will know if I need someone to help during the summer. So that's another certainty in there. You know, if you wanted to go through that pass you just have to live with that knowing, you know, that's, that's what you you, you're up for. But, you know, given the location I would say. That has location.

Speaker 1 (51:18)
Okay.

Speaker 2 (51:19)
San Francisco is just crossed the bridge. You can easily, you know, if you don't have class and you have to look easily, you know, hop on the train and get into the city and get a coffee with an alarm or someone that you're interested to talk to. You know, everyone's been through that and I'm sure you know people will open, people are open for that. People well, nowadays, everyone sort of a lot of people working from home which is tricky, but I'm sure if you reach

Speaker 1 (51:46)
Yeah.

Speaker 2 (51:46)
out to people on LinkedIn and be like, you know, I just wanted to You know, have a chat about, you know, your experience. My, you know, my experience has been amazing and so, you know, especially when it comes to reaching on so long in the same space and again, I think you're interested in the healthcare space. It's even smaller. And I would say more like tighter title community than the rest of the MBA program. And I'm sure you will get access to, you know, if you're interested in talk to someone graduate two years before you, I'm sure you can get connected.

Speaker 1 (52:22)
Okay. All right. Thank you very much. That'll be all.

Speaker 2 (52:26)
Okay, awesome. Yeah. So I will put these things in the scorecard and send it back to school. And I think, you know, you you should expect, you know, news the next steps from from the school.

Speaker 1 (52:42)
Thank you. Thank you so, so much.

Speaker 2 (52:43)
Yeah. Thanks for having my email if anything else comes up or if you know comes up or if you know At Indiana. You need to think through, you know, which school do I go to? I'm happy to have another conversation. If you have any questions down the road for me, All right.

Speaker 1 (53:1)
Alright, thank you. Thank you so much.

Speaker 2 (53:2)
Yeah.

Speaker 1 (53:3)
Thank you for your time.

Speaker 2 (53:5)
Bye.

Speaker 1 (53:6)
Bye.