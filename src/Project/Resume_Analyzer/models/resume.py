
from pydantic import BaseModel , Field


class Experience(BaseModel):
    company : str 
    role : str 
    durtation : float

class Project(BaseModel) : 
    name : str 
    description : str 
    technology : list[str]

class Certification(BaseModel):
    name : str 
    issuer : str 
    duration : float 
    description : str 
    skills_acquired : list[str]

class Resume(BaseModel):
    name : str
    email : str
    phone_number : int
    skills : list[str]
    experiences : list [Experience] = Field(default_factory=list)
    projects : list[Project] = Field(default_factory=list)
    certification : list[Certification] = Field(default_factory=list)


# schema creation 
resumeSchema = Resume.model_json_schema()