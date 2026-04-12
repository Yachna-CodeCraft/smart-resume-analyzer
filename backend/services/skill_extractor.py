import re
from .skills_db import SKILLS_DB, SYNONYMS


def normalize(text):
    text = text.lower()

    for k, v in SYNONYMS.items():
        text = text.replace(k, v)

    return text


def extract_skills(text):
    text = normalize(text)

    found = set()

    for skill in SKILLS_DB:
        if " " in skill:
            # multi-word skill
            if skill in text:
                found.add(skill)
        else:
            # single-word skill
            pattern = r'\b' + re.escape(skill) + r'\b'
            if re.search(pattern, text):
                found.add(skill)

    # remove duplicate concept
    if "spring boot" in found:
        found.discard("spring")

    return list(found)