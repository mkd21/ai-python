
import os

from groq import Groq
from dotenv import load_dotenv

load_dotenv()

groq_api_key = os.getenv("GROQ_API_KEY")

client = Groq(api_key=groq_api_key)


resume = """
    Mayank Deep
    Email: mayank@example.com

    Skills:
    Python, JavaScript, React, Node.js

    Experience:
    1 year of software development experience.

    Education:
    MCA
"""

from pydantic import BaseModel

# this structure will be followed 
class ResumeAnalysis(BaseModel):
    name : str
    email : str
    skills : list[str]
    experience_years : float
    education : list[str]


# schema creation 
schema = ResumeAnalysis.model_json_schema()

# response format 
response_format = {
    "type": "json_schema",
    "json_schema": {
        "name": "resume_analysis",
        "schema": schema
    }
}


response = client.chat.completions.create(

    model="llama-3.3-70b-versatile",

    messages= [ 
        {
            "role" : "system",
            "content" : "Analyze resumes and return the requested information in JSON format."
        },
        {
            "role" : "user",
            "content" : f"""
                Analyze this resume: 
                {resume}

            Return:
            name
            email
            skills
            experience_years,
            education
            """
        }
    ],
    response_format=response_format
)

# validating the LLM resposne 

jsonResponse = response.choices[0].message.content;

print(jsonResponse)