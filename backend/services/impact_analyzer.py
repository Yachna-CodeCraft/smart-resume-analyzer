def calculate_skill_impact(missing_skills):
    impact = {}

    for skill in missing_skills:
        impact[skill] = "+5% match improvement"

    return impact