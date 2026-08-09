

import os
from dotenv import load_dotenv
from groq import Groq

# making env variables available here
load_dotenv()


# getting groq api key 

api_key_groq = os.getenv("GROQ_API_KEY")

# gorq client 

client = Groq(api_key= api_key_groq)


message1 = "hi"
message2 = "hey, tell me about indian independence day"
message3 = "write an essay on ai and how its changing the world"

prompts = [message1 , message2 , message3]

for userMessage in prompts:

    message = { "role" : "user" , "content" : userMessage }

    response = client.chat.completions.create(

        model="llama-3.3-70b-versatile",
        messages= [message]
    )

    print(f"prompt token usage for ( {userMessage} ) is ",response.usage.prompt_tokens)
    print(f"completion token usage for ( {userMessage} ) is", response.usage.completion_tokens)
    print(f"total token usage for ( {userMessage} ) is", response.usage.total_tokens)
