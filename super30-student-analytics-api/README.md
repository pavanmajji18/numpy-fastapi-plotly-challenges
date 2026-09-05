# Super30 Student Analytics Engine

---

## Overview

The **Super30 Student Analytics Engine** bridges computational data science and production-grade API architecture. Rather than relying on slow, iterative Python loops or external database engines, student performance records are vectorized into continuous **NumPy $N$-dimensional arrays and matrices**. 

Aggregations, conditional cohort filtering, statistical dispersion metrics, and rankings execute with vectorized speed and are surfaced through **RESTful FastAPI GET endpoints** alongside **Plotly interactive visual dashboards**.

---

## System Architecture & Data Flow

```text
  [ Raw Student Data ]
           │
           ▼
  [ NumPy Vector Layer ] ────────┐
   • 2D Matrix (20x3)            │
   • Axis Reductions             │
   • Bitwise Boolean Masks       ▼
           │             [ Plotly Engine ]
           ▼              • HTML Interactive Charts
  [ FastAPI Endpoints ]   • Hover Tooltips & Zooms
   • Typed Responses             │
   • Exception Handlers          │
           │                     │
           ├─────────────────────┘
           ▼
  [ Client Browser / Swagger UI ]

```

---

## Directory Structure

```text
super30-student-analytics-api/
├── main.py              # Application core: Dataset, NumPy array pipeline, FastAPI routes
├── requirements.txt     # Pinned production dependencies
└── README.md            # Architecture specs, execution runbook, and cohort analysis

```

---

## Technology Stack

* **Runtime Framework:** [FastAPI](https://fastapi.tiangolo.com/) (Asynchronous ASGI framework with auto-generated OpenAPI schemas)
* **Computation Engine:** [NumPy](https://numpy.org/) (Multi-axis matrix operations, linear reductions, and boolean filtering)
* **Data Transport:** [Pandas](https://pandas.pydata.org/) (Lightweight tabular mapping for data visualization pipelines)
* **Visualization Layer:** [Plotly Express](https://plotly.com/python/) (D3.js-based interactive browser visualizations)
* **Application Server:** [Uvicorn](https://www.google.com/search?q=https://www.uvicorn.org/) (High-performance ASGI server)

---

## Quickstart & Installation

### 1. Clone the Repository

```bash
git clone [https://github.com/](https://github.com/)<your-username>/super30-student-analytics-api.git
cd super30-student-analytics-api

```

### 2. Configure Virtual Environment

```bash
# Unix / macOS
python3 -m venv venv
source venv/bin/activate

# Windows (Command Prompt / PowerShell)
python -m venv venv
venv\Scripts\activate

```

### 3. Install Locked Dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt

```

### 4. Launch Application Server

```bash
uvicorn main:app --reload --host 127.0.0.1 --port 8000

```

Once initialized, access:

* **Interactive OpenAPI (Swagger):** [http://127.0.0.1:8000/docs](https://www.google.com/url?sa=E&source=gmail&q=http://127.0.0.1:8000/docs)
* **ReDoc Documentation:** [http://127.0.0.1:8000/redoc](https://www.google.com/search?q=http://127.0.0.1:8000/redoc)

---

## API Documentation & Contract Reference

### Analytics & Data Endpoints

| Method | URI | NumPy Implementation Under the Hood | Output Description |
| --- | --- | --- | --- |
| `GET` | `/students` | Vector extraction | Returns full cohort of 20 students |
| `GET` | `/student/{id}` | `np.where(student_ids == id)` | Single student profile + calculated mean |
| `GET` | `/average/python` | `np.mean(python_scores)` | Cohort mean for Python |
| `GET` | `/average/mathematics` | `np.mean(math_scores)` | Cohort mean for Mathematics |
| `GET` | `/average/data-science` | `np.mean(ds_scores)` | Cohort mean for Data Science |
| `GET` | `/topper` | `np.argmax(student_averages)` | Full record of the highest-performing student |
| `GET` | `/passed` | `(P >= 40) & (M >= 40) & (DS >= 40)` | Students passing all three subjects |
| `GET` | `/failed` | `~pass_mask` (Bitwise NOT) | Students failing at least one subject |
| `GET` | `/statistics` | `np.mean`, `np.median`, `np.std`, `np.min`, `np.max` | Complete statistical cohort summary |

### Interactive Plotly Visualizations

| Method | URI | Visualization Type | Insights Rendered |
| --- | --- | --- | --- |
| `GET` | `/visualize/subject-averages` | Interactive Bar Chart | Compares global averages across Python, Mathematics, and Data Science |
| `GET` | `/visualize/top-students` | Interactive Bar Chart | Performance breakdown for the top 5 cohort leaders |

---

## Sample API Responses

### Top Performer (`GET /topper`)

```json
{
  "topper": {
    "id": 9,
    "name": "Pooja Reddy",
    "python": 95,
    "mathematics": 94,
    "data_science": 98,
    "overall_average": 95.67
  }
}

```

### Cohort Statistical Summary (`GET /statistics`)

```json
{
  "subject_averages": {
    "Python": 69.45,
    "Mathematics": 69.7,
    "Data Science": 72.8
  },
  "highest_marks": {
    "Python": 95,
    "Mathematics": 95,
    "Data Science": 98,
    "overall_highest": 98
  },
  "lowest_marks": {
    "Python": 30,
    "Mathematics": 25,
    "Data Science": 34,
    "overall_lowest": 25
  },
  "overall_average": 70.65,
  "overall_median": 78.0,
  "overall_std_dev": 22.42
}

```

---

## Analytical Findings & Academic Observations

NumPy vector reductions across the 20-student matrix yield five primary academic insights:

1. **Curricular Strength in Data Science:** Data Science recorded the highest subject mean (**72.80**), compared to Mathematics (**69.70**) and Python (**69.45**). It also recorded the highest single student score in the cohort (98 by Pooja Reddy).
2. **Clearance Rate (80% Pass Ratio):** Vectorized boolean filtering reveals that 16 of the 20 students met or exceeded the 40-mark passing benchmark in all three disciplines.
3. **Symmetric Multi-Subject Failure:** Among the 4 failed students (IDs: 3, 6, 12, 18), underperformance was non-isolated. A student failing Python systematically struggled in Mathematics, pointing to shared foundational gaps in analytical reasoning.
4. **Pronounced Cohort Bifurcation:** The 73-point spread between the lowest recorded score (25 in Mathematics) and the peak score (98 in Data Science), coupled with a standard deviation of **$\sigma \approx 22.42$**, indicates a bimodal skill distribution rather than a standard bell curve.
5. **Separation of the Top Quintile:** The top five students (Pooja Reddy, Ananya Iyer, Riya Sen, Tanvi Kapoor, Meera Rao) maintain overall averages strictly above **88.0%**, establishing a performance lead of more than 16 points over the cohort median.
