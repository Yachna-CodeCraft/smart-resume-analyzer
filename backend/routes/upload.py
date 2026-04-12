from fastapi import APIRouter, UploadFile, File, Form

from services.parser import extract_pdf, extract_docx, clean_text
from services.skill_extractor import extract_skills
from services.matcher import calculate_match
from services.scorer import calculate_resume_score

router = APIRouter()


@router.post("/analyze")
async def analyze_resume(
    file: UploadFile = File(...),
    job_description: str = Form(...)
):
    content = await file.read()

    # 🔹 Extract text
    if file.filename.endswith(".pdf"):
        text = extract_pdf(content)
    elif file.filename.endswith(".docx"):
        text = extract_docx(content)
    else:
        return {"error": "Unsupported file format"}

   
    cleaned_text = clean_text(text)

  
    resume_skills = extract_skills(cleaned_text)
    job_skills = extract_skills(job_description)


    print("JOB SKILLS:", job_skills)
    print("RESUME SKILLS:", resume_skills)


    match_score = calculate_match(
        cleaned_text,
        job_description,
        resume_skills,
        job_skills
    )


    matched_skills = list(set(resume_skills) & set(job_skills))
    missing_skills = list(set(job_skills) - set(resume_skills))

   
    resume_score = calculate_resume_score(
        cleaned_text,
        resume_skills,
        job_skills
    )

    
    suggestions = []

    if "aws" in missing_skills:
        suggestions.append("Learn AWS (EC2, S3 basics)")

    if "docker" in missing_skills:
        suggestions.append("Learn Docker for containerization")

    if "spring boot" in missing_skills:
        suggestions.append("Build a Spring Boot REST API project")

    if len(resume_skills) < 5:
        suggestions.append("Add more technical skills to resume")

    if not any(char.isdigit() for char in cleaned_text):
        suggestions.append("Add measurable achievements (e.g., improved performance by 30%)")

    return {
        "match_score": match_score,
        "resume_score": resume_score,
        "skills": resume_skills,
        "missing_skills": missing_skills,
        "suggestions": suggestions,
        "explanation": {
            "matched_skills": matched_skills,
            "missing_skills": missing_skills,
            "match_percentage": f"{len(set(resume_skills)&set(job_skills))}/{len(job_skills)} skills matched"

        }
    }