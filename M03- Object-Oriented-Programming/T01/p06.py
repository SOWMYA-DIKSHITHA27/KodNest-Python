# add readable output to job description

class JobDescription:
    def __init__(
        self,
        job_id,
        company,
        role,
        location,
        required_skills,
        is_active
    ): 
        self.job_id= job_id
        self.company = company
        self.role = role
        self.location = company
        self.required_skills = required_skills
        self.is_active = is_active
    def __str__(self):
        if self.is_active.strip().lower() == "yes":
            self.is_active = "Active"
        self.is_active = "Closed"
        return(f"JOB DESCRIPRION\n"
        f"Job ID: {self.job_id}\n"
        f"Company: {self.company}\n"
        f"Role: {self.role}\n"
        f"Location: {self.location}\n"  
        f"Required Skills: {self.required_skills}\n"
        f"Status: {self.is_active}")
job_id = input("Enter job_id   ").strip()
company = input("Enter company   ").strip()
role = input("Enter role   ").strip()
location = input("Enter location   ").strip()
required_skills = input("Enter comma sepated skills").strip()
status = input("Enter status as yes or no  ").strip()
job = JobDescription(job_id,
                     company,
                     role,
                     location,
                     required_skills,
                     status
                     )
print(job)