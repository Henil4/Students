from fastapi import FastAPI, Query
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
        row["class"] = row["class"].strip().upper()
        students_data.append(row)

@app.get("/api")
def get_students(class_: Optional[List[str]] = Query(default=None, alias="class")):
    print("tets")
    if class_:
        print("Test")
        filtered = [s for s in students_data if s["class"] in class_]
        return {"students": filtered}
    return {"students": students_data}
