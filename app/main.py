from fastapi import FastAPI
from datetime import datetime

app = FastAPI(
    title="DevOps Resume API",
    description="Cloud-native resume service showcasing DevOps capabilities",
    version="1.0.0"
)

@app.get("/")
def root():
    return {
        "message": "Welcome to the DevOps Resume API 🚀",
        "timestamp": datetime.utcnow()
    }

@app.get("/profile")
def get_profile():
    return {
        "name": "Neo Padi",
        "role": "DevOps Engineer",
        "location": "South Africa",
        "skills": [
            "GitHub Actions",
            "Docker",
            "CI/CD",
            "Monitoring",
            "FastAPI"
        ]
    }

@app.get("/health")
def health_check():
    return {"status": "ok"}