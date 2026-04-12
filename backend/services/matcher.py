from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer('all-MiniLM-L6-v2')

def calculate_match(text, job_desc, resume_skills, job_skills):
    # 🔹 Semantic similarity
    emb1 = model.encode(text, convert_to_tensor=True)
    emb2 = model.encode(job_desc, convert_to_tensor=True)

    semantic_score = float(util.cos_sim(emb1, emb2))  # 0–1

    # 🔹 Skill overlap
    overlap = 0
    if job_skills:
        overlap = len(set(resume_skills) & set(job_skills)) / len(job_skills)

    # 🔥 RULE 1: Perfect skill match → boost
    if job_skills and set(job_skills).issubset(set(resume_skills)):
        overlap = 1.0

    # 🔥 RULE 2: Balanced scoring
    final = (0.5 * semantic_score + 0.5 * overlap) * 100

    # 🔥 RULE 3: Cap logic (important)
    if overlap == 1.0:
        final = max(final, 90)  # ensure high score

    return round(final, 2)