from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from typing import List, Optional
import csv

app = FastAPI()

# Enable CORS for all origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load student data from CSV
students_data = []
with open("students.csv", newline='') as f:
    reader = csv.DictReader(f)
    for row in reader:
        row["studentId"] = int(row["studentId"])
        students_data.append(row)

@app.get("/api")
def get_students(class_: Optional[List[str]] = None):
    if class_:
        filtered = [s for s in students_data if s["class"] in class_]
        return {"students": filtered}
    return {"students": students_data}
