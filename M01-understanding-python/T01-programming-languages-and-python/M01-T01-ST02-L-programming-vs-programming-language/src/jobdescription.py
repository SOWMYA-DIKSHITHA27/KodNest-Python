class JobDescription:
    def __init__(self,job_id,company,role,location="Remote",minimum_score=0.0,required_skills=None,is_active=True):
        self.job_id=job_id
        self.company=company
        self.role=role
        self.location=location
        self.minimum_score=minimum_score
        self.required_skills=([] if required_skills is None else list(required_skills))
        self.is_active=is_active
    def __str__(self):
        skills_text=(",".join(self.required_skills) if self.required_skills else "Not specified")
        status="Active" if self.is_active else "Closed"
        return (
            f"Job ID: {self.job_id}\n"
            f"Company: {self.company}\n"
            f"Role: {self.role}\n"
            f"Location: {self.location}\n"
            f"Minimum Score: {self.minimum_score:.1f}\n"
            f"Required Skill: {skills_text}\n"
            f"Status: {self.is_active}\n"
        )
Job=JobDescription(
    job_id=101,
    company="Kodnest",
    role="Python Developer"
)
print(Job)
