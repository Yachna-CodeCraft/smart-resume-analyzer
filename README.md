# Smart Resume Analyzer

An AI-powered resume analysis platform that helps job seekers understand how well their resume matches a specific job description. The application analyzes the resume against the job requirements, calculates a similarity score, identifies relevant and missing skills, and provides actionable insights to improve the resume.

## 🚀 Features

* 📄 **Resume Upload** — Upload your resume for automated analysis.
* 📝 **Job Description Analysis** — Provide a target job description.
* 🎯 **Resume–JD Matching** — Compare resume content with job requirements.
* 📊 **Match Score** — Calculate an overall compatibility score using semantic/text similarity.
* 🧠 **Skill Extraction** — Identify technical skills and keywords present in the resume.
* ❌ **Missing Skills Detection** — Highlight important skills mentioned in the job description but missing from the resume.
* 💡 **Resume Improvement Suggestions** — Provide recommendations to improve alignment with the target role.
* 🔍 **Keyword Analysis** — Detect relevant keywords that can improve ATS compatibility.
* 📈 **Analysis Dashboard** — Present results in an easy-to-understand interface.

---

## 🏗️ System Architecture

```text
                    ┌─────────────────────┐
                    │       User          │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │   React Frontend    │
                    │                     │
                    │ Resume Upload       │
                    │ Job Description     │
                    │ Analysis Dashboard  │
                    └──────────┬──────────┘
                               │
                               │ API Requests
                               ▼
                    ┌─────────────────────┐
                    │   FastAPI Backend   │
                    │                     │
                    │ Resume Processing   │
                    │ Text Extraction     │
                    │ JD Processing       │
                    │ Similarity Analysis │
                    └──────────┬──────────┘
                               │
                    ┌──────────┴──────────┐
                    ▼                     ▼
          ┌──────────────────┐   ┌──────────────────┐
          │ NLP / Similarity │   │   Vector Store   │
          │     Engine       │   │                  │
          │                  │   │ Embeddings /     │
          │ Cosine Similarity│   │ Semantic Search  │
          └──────────────────┘   └──────────────────┘
                    │
                    ▼
          ┌─────────────────────┐
          │     Analysis        │
          │                     │
          │ Match Score         │
          │ Matched Skills      │
          │ Missing Skills      │
          │ Suggestions         │
          └─────────────────────┘
```

---

## 🛠️ Tech Stack

### Frontend

* React.js
* JavaScript
* HTML5
* CSS3
* Bootstrap / Tailwind CSS
* Axios
* Vite

### Backend

* Python
* FastAPI
* REST APIs

### AI / NLP

* Natural Language Processing
* Text Embeddings
* Cosine Similarity
* Semantic Similarity
* Keyword / Skill Extraction

### Database / Vector Storage

* ChromaDB
* Vector Embeddings

### Tools

* Git
* GitHub
* npm
* Python Virtual Environment

---

## 📂 Project Structure

```text
smart-resume-analyzer/
│
├── frontend/
│   ├── public/
│   ├── src/
│   │   ├── components/
│   │   ├── pages/
│   │   ├── services/
│   │   ├── App.jsx
│   │   └── main.jsx
│   ├── package.json
│   └── vite.config.js
│
├── backend/
│   ├── app/
│   │   ├── routes/
│   │   ├── services/
│   │   ├── models/
│   │   ├── utils/
│   │   └── main.py
│   ├── requirements.txt
│   └── .env
│
├── data/
│
├── README.md
└── .gitignore
```

> The exact structure may vary depending on the current implementation.

---

# 🔄 How It Works

### 1. Upload Resume

The user uploads their resume through the React interface.

```text
Resume → Backend → Text Extraction
```

The backend processes the uploaded document and extracts the relevant textual content.

### 2. Enter Job Description

The user provides the job description for the role they are targeting.

```text
Job Description → Text Processing
```

### 3. Process Resume and JD

The extracted resume and job description are cleaned and converted into representations that can be compared.

### 4. Generate Similarity

The system compares the resume and job description using text/semantic similarity.

One of the core approaches is **Cosine Similarity**:

```text
Similarity(A, B) = (A · B) / (||A|| × ||B||)
```

A higher similarity indicates stronger alignment between the resume and the job description.

### 5. Identify Skills

The analyzer compares the skills and keywords found in both documents.

Example:

```text
Resume Skills:
Java
React
MongoDB
Git

Job Requirements:
Java
React
MongoDB
AWS
Docker
Git

Matched:
✓ Java
✓ React
✓ MongoDB
✓ Git

Missing:
✗ AWS
✗ Docker
```

### 6. Generate Recommendations

The system provides suggestions based on the detected gaps.

For example:

```text
Your resume matches 78% of the job requirements.

Recommended improvements:
- Add relevant AWS experience if applicable.
- Mention Docker projects if you have worked with Docker.
- Include measurable project achievements.
```

---

# 📊 Example Analysis

### Input

**Job Role:** Full Stack Developer

### Resume

```text
Skills:
JavaScript
React
Node.js
MongoDB
Git
REST APIs
```

### Job Description

```text
Required:
React
Node.js
MongoDB
AWS
Docker
REST APIs
Git
```

### Result

```text
Match Score: 72%

Matched Skills:
✓ React
✓ Node.js
✓ MongoDB
✓ REST APIs
✓ Git

Missing Skills:
✗ AWS
✗ Docker
```

The analyzer then generates recommendations based on these gaps.

---

# 🧠 Core Concepts

## Cosine Similarity

Cosine similarity measures the similarity between two vectors by calculating the cosine of the angle between them.

```text
             A · B
Similarity = ───────
             |A||B|
```

The value generally ranges from:

```text
-1 → Completely opposite
 0 → No similarity
 1 → Highly similar
```

For resume matching, the score can be normalized and presented to users as a percentage.

---

## Vector Database

The project can use **ChromaDB** to store and retrieve vector representations of textual information.

This allows the system to perform semantic search and retrieve relevant information based on meaning rather than exact keyword matching.

---

# 🔌 API Overview

Example backend endpoints:

| Method | Endpoint          | Description               |
| ------ | ----------------- | ------------------------- |
| `POST` | `/upload-resume`  | Upload and process resume |
| `POST` | `/analyze`        | Analyze resume against JD |
| `POST` | `/extract-skills` | Extract skills from text  |
| `GET`  | `/health`         | Check API status          |

> Update these endpoints according to the actual routes implemented in the project.

---

# ⚙️ Installation

## Prerequisites

Make sure you have installed:

* Python 3.10+
* Node.js 18+
* npm
* Git

---

## 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/smart-resume-analyzer.git

cd smart-resume-analyzer
```

---

# 🖥️ Backend Setup

Navigate to the backend:

```bash
cd backend
```

Create a virtual environment:

```bash
python -m venv venv
```

### Windows

```bash
venv\Scripts\activate
```

### macOS / Linux

```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file:

```env
API_KEY=your_api_key
```

Run the FastAPI server:

```bash
uvicorn app.main:app --reload
```

The backend will be available at:

```text
http://localhost:8000
```

---

# 🌐 Frontend Setup

Open another terminal:

```bash
cd frontend
```

Install dependencies:

```bash
npm install
```

Start the development server:

```bash
npm run dev
```

The frontend will generally be available at:

```text
http://localhost:5173
```

---

# 🔐 Environment Variables

Never commit API keys or secrets to GitHub.

Example:

```env
API_KEY=your_api_key
```

Add sensitive files to `.gitignore`:

```gitignore
.env
venv/
__pycache__/
node_modules/
*.pyc
```

---

# 📈 Future Improvements

* [ ] AI-generated resume improvement suggestions
* [ ] ATS score prediction
* [ ] Support for multiple resume formats
* [ ] Job recommendation based on resume
* [ ] Resume section-wise scoring
* [ ] Experience-level detection
* [ ] Better semantic skill matching
* [ ] LinkedIn profile analysis
* [ ] Resume version comparison
* [ ] Personalized learning recommendations for missing skills
* [ ] Authentication and user profiles
* [ ] Resume history and analytics
* [ ] Deployment with production-grade infrastructure

---

# 🎯 Use Cases

### Students

Understand whether their resume matches internship and placement opportunities.

### Job Seekers

Identify missing skills and keywords before applying.

### Developers

Analyze technical alignment with software engineering roles.

### Career Preparation

Use job descriptions to identify which skills should be highlighted or developed.

---

# 🔒 Privacy

Resumes can contain sensitive personal information.

A production deployment should:

* Avoid permanently storing resumes unless necessary.
* Encrypt sensitive data.
* Secure uploaded files.
* Protect API endpoints.
* Never expose user resumes publicly.
* Remove temporary uploaded files after processing when possible.

---

# 🚀 Deployment

The application can be deployed using platforms such as:

```text
Frontend → Vercel / Netlify
Backend  → Render / Railway / AWS
Vector DB → ChromaDB / managed vector database
```

For production deployment, configure environment variables and CORS appropriately.

---

# 📸 Screenshots

Add screenshots of the application here:

```text
docs/
├── dashboard.png
├── resume-upload.png
├── analysis-result.png
└── skill-analysis.png
```

Example:

```markdown
![Dashboard](docs/dashboard.png)

![Analysis Result](docs/analysis-result.png)
```

---

# 💡 Why This Project?

Traditional resume screening often relies heavily on keywords. This project explores how NLP, vector representations, and similarity techniques can be used to provide a more meaningful comparison between a candidate's resume and a specific job description.

The goal is not to replace recruiters but to help candidates understand **how well their resume communicates their relevant skills and experience for a particular role.**

---

# 👩‍💻 Author

**Yachna**

B.Tech – Computer Science & Engineering

Interested in:

* Full Stack Development
* AI/ML
* Natural Language Processing
* Data Structures & Algorithms
* Software Engineering

---

# ⭐ Contributing

Contributions are welcome.

1. Fork the repository.
2. Create a feature branch.

```bash
git checkout -b feature/new-feature
```

3. Commit your changes.

```bash
git commit -m "Add new feature"
```

4. Push the branch.

```bash
git push origin feature/new-feature
```

5. Open a Pull Request.

---

# 📄 License

This project is licensed under the MIT License.
