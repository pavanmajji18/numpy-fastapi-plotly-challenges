import logging
from typing import Any

from fastapi import FastAPI, HTTPException, status
from fastapi.responses import HTMLResponse
import numpy as np
import pandas as pd
import plotly.express as px

# --- Logging Setup ---
logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
logger = logging.getLogger(__name__)

# --- FastAPI App Initialization ---
app = FastAPI(title="Student Analytics API", version="1.0.0")

# --- Dataset: 20 Students (ID, Name, Python, Mathematics, Data Science) ---
students_data = [
    {"id": 1, "name": "Aarav Sharma", "python": 85, "mathematics": 78, "data_science": 90},
    {"id": 2, "name": "Diya Patel", "python": 72, "mathematics": 88, "data_science": 82},
    {"id": 3, "name": "Rohan Verma", "python": 40, "mathematics": 35, "data_science": 42},
    {"id": 4, "name": "Ananya Iyer", "python": 92, "mathematics": 95, "data_science": 96},
    {"id": 5, "name": "Kavya Nair", "python": 78, "mathematics": 65, "data_science": 70},
    {"id": 6, "name": "Ishaan Gupta", "python": 30, "mathematics": 25, "data_science": 35},
    {"id": 7, "name": "Meera Rao", "python": 88, "mathematics": 91, "data_science": 85},
    {"id": 8, "name": "Arjun Singh", "python": 62, "mathematics": 58, "data_science": 64},
    {"id": 9, "name": "Pooja Reddy", "python": 95, "mathematics": 94, "data_science": 98},
    {"id": 10, "name": "Aditya Joshi", "python": 45, "mathematics": 48, "data_science": 52},
    {"id": 11, "name": "Neha Kulkarni", "python": 80, "mathematics": 84, "data_science": 79},
    {"id": 12, "name": "Siddharth Das", "python": 38, "mathematics": 42, "data_science": 39},
    {"id": 13, "name": "Tanvi Kapoor", "python": 89, "mathematics": 90, "data_science": 92},
    {"id": 14, "name": "Varun Bhat", "python": 67, "mathematics": 70, "data_science": 65},
    {"id": 15, "name": "Riya Sen", "python": 91, "mathematics": 89, "data_science": 93},
    {"id": 16, "name": "Karan Malhotra", "python": 52, "mathematics": 49, "data_science": 55},
    {"id": 17, "name": "Sneha Ghosh", "python": 84, "mathematics": 82, "data_science": 86},
    {"id": 18, "name": "Manish Tiwari", "python": 32, "mathematics": 38, "data_science": 34},
    {"id": 19, "name": "Pooja Choudhury", "python": 76, "mathematics": 74, "data_science": 78},
    {"id": 20, "name": "Rahul Deshmukh", "python": 83, "mathematics": 85, "data_science": 87},
]

# --- NumPy Array Extractions & Matrix Operations ---
student_ids = np.array([s["id"] for s in students_data])
python_scores = np.array([s["python"] for s in students_data])
math_scores = np.array([s["mathematics"] for s in students_data])
ds_scores = np.array([s["data_science"] for s in students_data])

# 2D Matrix of scores (shape: 20 rows, 3 columns)
# Col 0: Python, Col 1: Mathematics, Col 2: Data Science
score_matrix = np.array([
    [s["python"], s["mathematics"], s["data_science"]]
    for s in students_data
])

# Row-wise means (overall average per student)
student_averages = np.mean(score_matrix, axis=1)

# Pass criterion: Every subject mark >= 40 (using boolean masking)
pass_mask = (python_scores >= 40) & (math_scores >= 40) & (ds_scores >= 40)
fail_mask = ~pass_mask


# ---------------- API ENDPOINTS ----------------

# 1. GET /students
@app.get("/students")
def get_all_students() -> dict[str, Any]:
    logger.info("Fetching all students")
    return {"total_students": len(students_data), "students": students_data}


# 2. GET /student/{student_id}
@app.get("/student/{student_id}")
def get_student(student_id: int) -> dict[str, Any]:
    logger.info("Fetching student details for ID: %d", student_id)
    # Boolean masking to find target ID
    match_indices = np.where(student_ids == student_id)[0]
    if match_indices.size == 0:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Student with ID {student_id} not found",
        )
    idx = match_indices[0]
    student_record = dict(students_data[idx])
    student_record["average"] = float(round(student_averages[idx], 2))
    return {"student": student_record}


# 3. GET /average/python
@app.get("/average/python")
def get_python_average() -> dict[str, Any]:
    avg = np.mean(python_scores)
    return {"subject": "Python", "average": float(round(avg, 2))}


# 4. GET /average/mathematics
@app.get("/average/mathematics")
def get_math_average() -> dict[str, Any]:
    avg = np.mean(math_scores)
    return {"subject": "Mathematics", "average": float(round(avg, 2))}


# 5. GET /average/data-science
@app.get("/average/data-science")
def get_data_science_average() -> dict[str, Any]:
    avg = np.mean(ds_scores)
    return {"subject": "Data Science", "average": float(round(avg, 2))}


# 6. GET /topper
@app.get("/topper")
def get_topper() -> dict[str, Any]:
    top_idx = int(np.argmax(student_averages))
    topper = dict(students_data[top_idx])
    topper["overall_average"] = float(round(student_averages[top_idx], 2))
    return {"topper": topper}


# 7. GET /passed
@app.get("/passed")
def get_passed_students() -> dict[str, Any]:
    passed_ids = student_ids[pass_mask]
    passed_records = [s for s in students_data if s["id"] in passed_ids]
    return {
        "criterion": "Marks >= 40 in every subject",
        "passed_count": int(np.sum(pass_mask)),
        "students": passed_records,
    }


# 8. GET /failed
@app.get("/failed")
def get_failed_students() -> dict[str, Any]:
    failed_ids = student_ids[fail_mask]
    failed_records = [s for s in students_data if s["id"] in failed_ids]
    return {
        "criterion": "Marks < 40 in at least one subject",
        "failed_count": int(np.sum(fail_mask)),
        "students": failed_records,
    }


# 9. GET /statistics
@app.get("/statistics")
def get_statistics() -> dict[str, Any]:
    # Matrix reductions: axis=0 computes column-wise stats across subjects
    col_means = np.mean(score_matrix, axis=0)

    return {
        "subject_averages": {
            "Python": float(round(col_means[0], 2)),
            "Mathematics": float(round(col_means[1], 2)),
            "Data Science": float(round(col_means[2], 2)),
        },
        "highest_marks": {
            "Python": int(np.max(python_scores)),
            "Mathematics": int(np.max(math_scores)),
            "Data Science": int(np.max(ds_scores)),
            "overall_highest": int(np.max(score_matrix)),
        },
        "lowest_marks": {
            "Python": int(np.min(python_scores)),
            "Mathematics": int(np.min(math_scores)),
            "Data Science": int(np.min(ds_scores)),
            "overall_lowest": int(np.min(score_matrix)),
        },
        "overall_average": float(round(np.mean(score_matrix), 2)),
        "overall_median": float(round(np.median(score_matrix), 2)),
        "overall_std_dev": float(round(np.std(score_matrix), 2)),
    }


# 10. GET /visualize/subject-averages (Plotly Bar Chart)
@app.get("/visualize/subject-averages", response_class=HTMLResponse)
def visualize_subject_averages():
    df = pd.DataFrame({
        "Subject": ["Python", "Mathematics", "Data Science"],
        "Average Marks": [
            float(round(np.mean(python_scores), 2)),
            float(round(np.mean(math_scores), 2)),
            float(round(np.mean(ds_scores), 2)),
        ],
    })
    fig = px.bar(
        df,
        x="Subject",
        y="Average Marks",
        title="Average Marks Across Subjects",
    )
    return HTMLResponse(content=fig.to_html(full_html=True))


# 11. GET /visualize/top-students (Plotly Top 5 Comparison Bar Chart)
@app.get("/visualize/top-students", response_class=HTMLResponse)
def visualize_top_students():
    # Sort descending by overall average using NumPy argsort
    top_indices = np.argsort(student_averages)[::-1][:5]

    top_names = [students_data[i]["name"] for i in top_indices]
    top_scores = [float(round(student_averages[i], 2)) for i in top_indices]

    df = pd.DataFrame({
        "Student": top_names,
        "Overall Average": top_scores,
    })
    fig = px.bar(
        df,
        x="Student",
        y="Overall Average",
        title="Top 5 Students by Overall Average",
    )
    return HTMLResponse(content=fig.to_html(full_html=True))