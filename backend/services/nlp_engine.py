def extract_skills(text):
    skills_db = ["Python", "Java", "React", "Node.js", "MongoDB", "MySQL"]

    found_skills = []

    for skill in skills_db:
        if skill.lower() in text.lower():
            found_skills.append(skill)

    return found_skills