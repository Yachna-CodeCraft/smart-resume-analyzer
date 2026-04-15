from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import upload

# Initialize FastAPI app
app = FastAPI()

# Include routes
app.include_router(upload.router)

# CORS (important for frontend connection)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, restrict this
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Root route (for testing)
@app.get("/")
def home():
    return {"message": "Server is running successfully 🚀"}