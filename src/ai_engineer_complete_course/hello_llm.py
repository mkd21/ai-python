
import os
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq

load_dotenv()  # this method will make env variables available here 

my_api_key = os.getenv("GROQ_API_KEY")

if not my_api_key:
    raise ValueError("Api key missing...")


# create Groq client
client = Groq(api_key=my_api_key)


# # call the model 

response = client.chat.completions.create(

    model="llama-3.3-70b-versatile",

    messages= [
        {
            "role" : "user",
            "content" : "What work kpmg does? keep it short"
        }
    ]
)

print(response.choices[0].message.content)