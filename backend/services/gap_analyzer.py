def find_skill_gap(resume_skills, job_skills):
    """
    Find missing skills from resume compared to job
    """

    resume_set = set([s.lower() for s in resume_skills])
    job_set = set([s.lower() for s in job_skills])

    missing = job_set - resume_set

    return list(missing)