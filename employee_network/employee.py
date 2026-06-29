from dataclasses import dataclass

@dataclass
class Employee:
    registration_number: str
    age: int
    gender: str
    education_level: str
    job_title: str
    years_of_experience: int
    salary: int
