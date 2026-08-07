
import os
from groq import Groq
from dotenv import load_dotenv as Dotenv

Dotenv()

groq_api_key = os.getenv('GROQ_API_KEY')

# create groq client 

groq_client = Groq(api_key = groq_api_key)

# call the model 

response = groq_client.chat.completions.create(

    model= "llama-3.3-70b-versatile",

    messages= [
        {
            'role' : "system",
            'content' : "you are a product designer"
        },
        {
            'role' : "user",
            "content" : "i have a startup which delivers food with no extra charges, what name should i keep for the app. suggest only one name"
        }
    ],

    temperature = 2
)

print( response.choices[0].message.content)