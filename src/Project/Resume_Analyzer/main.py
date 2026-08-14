
from .services.llm_service import client
from .models.job_description import Job_Description_schema

job_description = """


Software Engineer - Backend

TechNova Solutions Pvt. Ltd.** is looking for a Software Engineer to join our backend engineering team in Bengaluru, Karnataka. This is a full-time, on-site position with an annual compensation range of ₹8,00,000 to ₹12,00,000, depending on experience and skills.

About the Role

The ideal candidate will have around **2 years of professional software development experience** and will work closely with frontend engineers, product managers, and other backend developers to build reliable and scalable applications.

Key Responsibilities

* Design, develop, and maintain backend services and RESTful APIs.
* Build scalable and maintainable server-side applications using Node.js.
* Design database schemas and write efficient queries for application data.
* Integrate third-party APIs and external services into backend systems.
* Write unit and integration tests and troubleshoot production issues.
* Participate in code reviews and contribute to engineering best practices.
* Collaborate with frontend developers to ensure smooth API integration.
* Monitor application performance and improve system reliability.

Required Skills

Candidates should have strong hands-on experience with:

* JavaScript
* Node.js
* Express.js
* REST APIs
* MongoDB
* Git and GitHub

Experience with asynchronous programming, API authentication, and basic software design principles is also expected.

### Preferred Skills

The following skills would be an advantage:

* TypeScript
* PostgreSQL
* Docker
* Redis
* AWS
* CI/CD pipelines

Educational Qualifications

Applicants must have a **Bachelor's degree in Computer Science, Information Technology, Software Engineering, or a related technical field**.

A **Master's degree in Computer Science, Information Technology, or a related discipline** will be considered an additional advantage.

Experience & Seniority

* Minimum experience required: **2 years**
* Seniority: **Mid-Level**
* Experience working in a production software development environment is required.

Employment Details

* **Employment Type:** Full-time
* **Work Mode:** On-site
* **Location:** Bengaluru, Karnataka, India
* **Salary:** ₹8,00,000 - ₹12,00,000 per year

Company

TechNova Solutions Pvt. Ltd. is a software technology company that develops cloud-based business applications for startups and enterprises.


"""


system_prompt = f"""

    You are a job description information extraction assistant.

    Your task is to extract all relevant information from the provided job description and structure it according to the given JSON schema.

    Rules:

    1. Extract information only from the provided job description.
    2. Map the information from the job description to the corresponding fields in the JSON schema.
    3. Do not invent, assume, or add information that is not present in the job description.
    4. If an optional field is not mentioned, set its value to null.
    5. If a list field has no information available, return an empty list.
    6. Preserve the meaning of the original information while normalizing it into the required data types.
    7. Convert numerical values to the appropriate numeric type where possible. For example, "2 years" should become 2.
    8. Return only the structured JSON data matching the provided schema.
    9. Do not include explanations, comments, markdown, or additional fields.
    10. Ensure that all fields required by the schema are present in the output.

    The JSON schema that defines the required output structure is provided below

    {Job_Description_schema}

"""

user_prompt = f"""
    Analyze the following job description and extract all relevant information according to the provided JSON schema.

    Job Description:
    {job_description}
"""

response_format = {
    "type" : "json_object"
}

response = client.chat.completions.create(

    model="llama-3.3-70b-versatile",

    messages= [ 
        { "role" : "system" , "content" : system_prompt } , 
        {  "role" : "user" , "content" : user_prompt} 
    ],

    response_format=response_format
)

answer = response.choices[0].message.content

print(answer)