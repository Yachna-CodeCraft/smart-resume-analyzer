def calculate_resume_score(text, skills, job_skills=None):
    score = 70  # base

    if job_skills:
        matched = len(set(skills) & set(job_skills))
        total = len(job_skills)

        if total > 0:
            score = score * (matched / total)

    if len(text.split()) > 120:
        score += 10

    if any(w in text.lower() for w in ["project", "experience"]):
        score += 10
    if set(job_skills).issubset(set(skills)):
        match_score = 100
    return round(min(score, 100), 2)