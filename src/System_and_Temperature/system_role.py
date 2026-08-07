
import os

from groq import Groq
from pathlib import Path
from dotenv import load_dotenv


load_dotenv()

groq_api_key = os.getenv("GROQ_API_KEY")

if not groq_api_key:
    raise ValueError("Api key missing")


# creating groq client 
groqClient = Groq(api_key=groq_api_key)


message_system = {
    "role" : "system",
    "content" : "you are my colleague and strict manager in a compay we both work"
}

# message_system = {
#     "role" : "system",
#     "content" : "you are my lving girlfriend"
# }

role = "user"
content = "i love you babe"

message_user = {
    "role" : role,
    "content" : content
}

response = groqClient.chat.completions.create(

    model="llama-3.3-70b-versatile",

    messages= [ message_system , message_user ]
)

print(response.choices[0].message.content);