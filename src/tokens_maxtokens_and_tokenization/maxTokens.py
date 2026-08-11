
import os

from dotenv import load_dotenv
from groq import Groq


load_dotenv()  # will make env variables available here

api_groq = os.getenv("GROQ_API_KEY")


# groq client 
client = Groq(api_key=api_groq)


userMessage1 = "hi"
userMessage2 = "write an essay on how technology is shaping the future of our world"
userMessage3 = "give me a startup idea in food delivery or generic delivery domain which will have potential to grow"

messages = [userMessage1 , userMessage2 , userMessage3]


for prompt in messages:

    messageByUser = { "role" : "user" , "content" : prompt }

    response = client.chat.completions.create(

        model="llama-3.3-70b-versatile",
        messages= [messageByUser],
        max_tokens=500
    )

    print(f"prompt tokens consumed for {prompt} is {response.usage.prompt_tokens}" )

    print(f"completion tokens consumed for {prompt} is {response.usage.completion_tokens}")

    print(f"total tokens consumed for {prompt} is", response.usage.prompt_tokens )

    print(f"exectution stopped because of {response.choices[0].finish_reason}")


# if LLM stops after completing the word then the reason will be "STOP" but if it stops because of token limit then

# finish reason will be "LENGTH"