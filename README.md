<div align="center">

# 🚀 Super30: NumPy, FastAPI & Plotly Challenge Suite

**A comprehensive repository of production-ready Python projects combining vectorized numerical processing (NumPy), asynchronous RESTful microservices (FastAPI), tabular data handling (Pandas), and dynamic web visualizations (Plotly).**

[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white)](#)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.110%2B-009688?logo=fastapi&logoColor=white)](#)
[![NumPy](https://img.shields.io/badge/NumPy-Vectorized-013243?logo=numpy&logoColor=white)](#)
[![Plotly](https://img.shields.io/badge/Plotly-Interactive%20Charts-3F4F75?logo=plotly&logoColor=white)](#)
[![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458?logo=pandas&logoColor=white)](#)
[![Code Style](https://img.shields.io/badge/Code%20Style-Black-000000)](#)

</div>

---

## 📌 Repository Overview

This repository contains **6 distinct hands-on projects and challenge modules** developed under the **Euron Super30 Python Track**. The suite spans fundamental array mechanics to full-stack data analytics services that combine NumPy vectorized data engines with FastAPI backends and Plotly web graphics.

---

## 📂 Architecture & Directory Layout

```text
numpy-fastapi-plotly-challenges/
│
├── ⚡ super30-fastapi-get-api-task/       # 12 GET APIs for basic FastAPI routing & logic
│   ├── main.py
│   ├── requirements.txt
│   └── README.md
│
├── 🔢 super30-fastapi-numpy-api/          # RESTful statistical engine powered by NumPy
│   ├── main.py
│   ├── requirements.txt
│   └── README.md
│
├── 📈 super30-numpy-plotly-analytics/     # Business financial analytics & Plotly dashboard
│   ├── main.py
│   ├── output.txt
│   ├── requirements.txt
│   └── README.md
│
├── 🧮 super30-numpy-task-1/               # 12 Pure NumPy computational problem solutions
│   ├── main.py
│   ├── output.txt
│   ├── requirements.txt
│   └── README.md
│
├── 📊 super30-plotly-visualization-Challenge/ # 12 FastAPI endpoints serving interactive Plotly charts
│   ├── main.py
│   ├── requirements.txt
│   └── README.md
│
└── 🎓 super30-student-analytics-api/      # Student cohort analytics engine (NumPy + FastAPI + Plotly HTML)
    ├── main.py
    ├── requirements.txt
    ├── response_1788749576399.html
    └── README.md
```

---

## 🛠️ Detailed Module Breakdown

### 1. ⚡ `super30-fastapi-get-api-task` — FastAPI Route Foundations
Demonstrates building basic GET microservices in FastAPI with static endpoints, path parameters, string formatting, and conditional logic.

* **Core Focus:** Path parameters (`{num1}`, `{name}`, `{age}`), route handling, OpenAPI Swagger generation.
* **Key Endpoints:**
  * `GET /` — Welcome message
  * `GET /student` & `GET /course` & `GET /skills` — Static details & list returns
  * `GET /add/{num1}/{num2}` & `GET /multiply/{num1}/{num2}` — Mathematical operations
  * `GET /square/{number}` & `GET /table/{number}` — Arithmetic transformations
  * `GET /check/{number}` & `GET /age/{age}` — Conditional logic & age category classification
  * `GET /profile/{name}/{age}` & `GET /number/{number}` — Comprehensive payload output (square, cube, parity)

---

### 2. 🔢 `super30-fastapi-numpy-api` — Vectorized Statistical API
Exposes statistical reduction operations over a base NumPy numerical array (`np.array([12, 15, 23, 42, 56, 78, 89, 90, 34, 67, 18, 99])`) via high-speed REST endpoints.

* **Core Focus:** Vectorized aggregation methods (`np.mean`, `np.median`, `np.std`, `np.var`, `np.min`, `np.max`, `np.sum`), boolean indexing (`data % 2 == 0`).
* **Key Endpoints:**
  * `GET /numbers` — Raw numerical array output
  * `GET /mean`, `GET /median`, `GET /std`, `GET /variance` — Statistical indicators
  * `GET /maximum`, `GET /minimum`, `GET /sum` — Extrema and summation
  * `GET /even`, `GET /odd` — Boolean mask filtered arrays
  * `GET /stats` — Consolidated full statistical report
  * `GET /table/{number}` — Vectorized multiplication table using `np.arange`

---

### 3. 📈 `super30-numpy-plotly-analytics` — Corporate Financial Analytics Engine
Simulates and analyzes a company's annual financial cycle over 12 months using element-wise array arithmetic and renders interactive Plotly management dashboards.

* **Core Focus:** 
  * Financial calculations: Net Profit (`Revenue - Expenses`), Month-over-Month Revenue Differences (`revenue[1:] - revenue[:-1]`).
  * Metrics computed: Total/Average Revenue & Profit, Peak Performance Month identification (`np.argmax`).
* **Plotly Visualizations Rendered:**
  * Line Chart: Monthly Revenue Trend
  * Bar Chart: Monthly Order Volume & Monthly Net Profit
  * Grouped Bar Chart: Monthly Revenue vs. Expenses Comparison
  * Area Chart: Cumulative Customer Base Growth
  * Executive Overview Dashboard: Multi-trace combination of cash flows and net profitability line overlay

---

### 4. 🧮 `super30-numpy-task-1` — 12 Core NumPy Computational Challenges
A standalone suite solving 12 foundational NumPy problems spanning 1D and 2D tensor operations.

* **Problems Solved:**
  1. **Array Creation:** `np.arange` for 1-50, evens (2-100), and odds (1-99).
  2. **Student Marks Analysis:** Aggregations (`sum`, `mean`, `max`, `min`, `median`) on 10 student scores.
  3. **Boolean Filtering:** Extracting marks `> 90`, `> mean`, and `< 70`.
  4. **Reshaping:** Transforming a 1D array of 20 elements into a $4 \times 5$ 2D matrix.
  5. **2D Matrix Operations:** Slice extraction (Row 0, Col 1, Element $[1,2]$) from a $3 \times 3$ grid.
  6. **Mathematical Operations:** Element-wise addition, subtraction, multiplication, and division.
  7. **Statistical Analysis:** Normal distribution generation (`np.random.normal(0, 1, 100)`) & dispersion metrics.
  8. **Sorting:** Ascending and descending (`[::-1]`) array reordering.
  9. **Unique Values:** Deduplication using `np.unique`.
  10. **Matrix Arithmetic & Dot Product:** Matrix addition, subtraction, element-wise product, and matrix dot product (`@`).
  11. **Salary Analysis:** Filtering and analyzing employee salary distributions.
  12. **5x5 Matrix Challenge:** Random integer grid (`1-100`), global extrema, row sums (`axis=1`), column sums (`axis=0`).

---

### 5. 📊 `super30-plotly-visualization-Challenge` — Interactive Web Charting Server
A FastAPI service with 12 distinct routes, each generating and opening interactive Plotly web visualizers for business, academic, and statistical scenarios.

* **Endpoints & Chart Types:**
  * `GET /monthly-sales-bar` — Interactive Bar Chart
  * `GET /monthly-sales-line` — Line Chart with Markers
  * `GET /department-distribution-pie` — Pie Chart (Employee Distribution)
  * `GET /study-marks-scatter` — Scatter Plot (Hours vs. Marks)
  * `GET /random-values-histogram` — Gaussian Distribution Histogram
  * `GET /employee-salary-box` — Box Plot with Outlier Analysis
  * `GET /product-sales-grouped-bar` — Grouped Product Sales (Laptop, Mobile, Tablet)
  * `GET /student-performance-bar` — Multi-subject Student Comparison
  * `GET /age-salary-scatter3d` — 3D Scatter Plot (Age, Salary, Experience)
  * `GET /conversion-funnel` — Conversion Funnel Stage Chart
  * `GET /numpy-random-line` — Line Plot of NumPy Random Noise
  * `GET /company-dashboard` — 4-Panel Executive Subplot Dashboard (`make_subplots`)

---

### 6. 🎓 `super30-student-analytics-api` — End-to-End Academic Intelligence System
Combines FastAPI, 2D NumPy matrix operations, Pandas DataFrames, and embedded HTML Plotly visualizations to perform student cohort analysis for 20 students across 3 subjects (Python, Math, Data Science).

* **Core Features:**
  * Vectorized 2D score matrix ($20 \times 3$) and axis reductions (`axis=1` for student means, `axis=0` for subject means).
  * Vectorized boolean pass mask: `(Python >= 40) & (Math >= 40) & (DS >= 40)`.
  * Dynamic Plotly chart generation returned directly as `HTMLResponse`.
* **Key Endpoints:**
  * `GET /students` — Full cohort record
  * `GET /student/{id}` — Individual profile & calculated average via `np.where`
  * `GET /average/{subject}` — Subject cohort means
  * `GET /topper` — Highest performing student (`np.argmax`)
  * `GET /passed` & `GET /failed` — Filtered student lists based on boolean masks
  * `GET /statistics` — Complete matrix dispersion report (`mean`, `median`, `std`, `min`, `max`)
  * `GET /visualize/subject-averages` — Interactive HTML Bar Chart of subject means
  * `GET /visualize/top-students` — Interactive HTML Bar Chart of Top 5 cohort leaders

---

## 💻 Tech Stack & Requirements

| Layer | Technology | Purpose |
| --- | --- | --- |
| **Language** | Python 3.10+ | Core application runtime |
| **API Framework** | FastAPI + Uvicorn | Asynchronous REST microservices & ASGI server |
| **Numeric Engine** | NumPy | Multidimensional matrix algebra & vectorized calculations |
| **Data Frames** | Pandas | Data wrangling and chart data structure binding |
| **Visualizations** | Plotly (Express & Graph Objects) | Interactive D3.js browser graphics & HTML rendering |

---

## ⚡ Quickstart & Local Setup

### 1. Clone the Workspace
```bash
git clone https://github.com/pavanmajji18/numpy-fastapi-plotly-challenges.git
cd numpy-fastapi-plotly-challenges
```

### 2. Set Up a Virtual Environment
```bash
# On Windows (PowerShell)
python -m venv venv
.\venv\Scripts\activate

# On macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Run Standalone NumPy & Plotly Projects
For pure Python execution (e.g., `super30-numpy-task-1` or `super30-numpy-plotly-analytics`):
```bash
# Execute standalone NumPy challenges
python super30-numpy-task-1/main.py

# Execute financial analytics & launch Plotly charts
python super30-numpy-plotly-analytics/main.py
```

### 4. Run FastAPI Servers
To launch any of the FastAPI application servers, navigate to the respective folder or specify the path:

```bash
# Example 1: Launch Student Analytics Engine
cd super30-student-analytics-api
pip install -r requirements.txt
uvicorn main:app --reload --port 8000
```

Once running, explore the auto-generated Swagger UI at:
* **Interactive OpenAPI Docs:** `http://127.0.0.1:8000/docs`
* **ReDoc Interface:** `http://127.0.0.1:8000/redoc`

---

## 🎯 Key Learning Outcomes

1. **Vectorized Computation:** Eliminated slow `for` loops in favor of contiguous NumPy array broadcasting, matrix dot products, and multi-axis reductions.
2. **High-Performance APIs:** Designed RESTful microservices with FastAPI enforcing typed parameters, custom status codes, and exception management.
3. **Interactive Data Storytelling:** Transformed raw numerical arrays into dynamic interactive web charts (2D, 3D, subplots, funnels) with Plotly.
4. **Full-Stack Data Engineering:** Combined backend data pipelines, numeric matrix algebra, and web visualization into cohesive production-ready microservices.

---

<div align="center">
  <sub>Built with ❤️ during the Euron Super30 Python Track</sub>
</div>
