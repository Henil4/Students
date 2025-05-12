from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from typing import List
import csv
import os

app = FastAPI()

# CORS for all origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load data once at startup
students_data = []
csv_path = os.path.join(os.path.dirname(__file__), "..", "students.csv")
with open(csv_path, newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        row["studentId"] = int(row["studentId"])
        students_data.append(row)

@app.get("/")
def home():
    return {"status": "FastAPI running on Vercel"}

@app.get("/api")
def get_students(class_: List[str] = None):
    if class_:
        return {"students": [s for s in students_data if s["class"] in class_]}
    return {"students": students_data}
