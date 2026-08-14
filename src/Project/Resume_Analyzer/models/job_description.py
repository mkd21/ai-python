

from pydantic import BaseModel , Field

class Job_Description(BaseModel):

    title : str
    company : str 
    location : str 
    employment_type : str 
    work_mode : str 
    salary : float | None = None

    description : str 
    experience_required : float | None = None
    seniority_level : str

    required_skills : list[str]
    preferred_skills : list[str]

    responsiblities : list[str]

    required_qualifications : list[str]
    preferred_qualifications : list[str]

    
Job_Description_schema = Job_Description.model_json_schema()