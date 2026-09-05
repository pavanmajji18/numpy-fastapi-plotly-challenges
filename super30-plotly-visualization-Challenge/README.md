# Super30 Plotly Visualization Challenge

Convert raw data into meaningful, interactive data visualizations using Plotly Express, Plotly Graph Objects, NumPy, and Pandas, with interactive API execution via FastAPI and Swagger UI.

---

**Author Information**

* **Student Name:** Pavan Kumar Majji


* **Project Name:** super30-plotly-task-2 / super30-plotly-visualization-Challenge

---

**Repository Structure**

```text
super30-plotly-visualization-Challenge/
│
├── main.py
├── requirements.txt
└── README.md

```

---

**Installation & Environment Setup**

1. Clone or open the repository folder:


```bash
cd super30-plotly-visualization-Challenge

```


2. Install the necessary dependencies:


```bash
pip install -r requirements.txt

```



---

**How to Run the Server**

Start the FastAPI application using the Uvicorn server:

```bash
uvicorn main:app --reload --port 8000

```

Once the server is running, open the interactive Swagger UI in your browser:

* **Interactive API Documentation:** `[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)`

From the Swagger UI interface, click on any endpoint, click **"Try it out"**, and press **"Execute"**. The endpoint triggers Plotly's interactive rendering engine (`fig.show()`) and automatically opens the visualization in a new browser tab.

---

**Available API Endpoints & Example URLs**

| # | Chart Type | Endpoint Path | Full Example URL | Description |
| --- | --- | --- | --- | --- |
| **Doc** | Swagger UI | `/docs` | `[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)` | Interactive Swagger testing console |
| **1** | Bar Chart | `/monthly-sales-bar` | `[http://127.0.0.1:8000/monthly-sales-bar](http://127.0.0.1:8000/monthly-sales-bar)`<br> | Monthly sales for 6 months (`Jan` to `Jun`)

 |
| **2** | Line Chart | `/monthly-sales-line` | `[http://127.0.0.1:8000/monthly-sales-line](http://127.0.0.1:8000/monthly-sales-line)`<br> | Trend view of monthly sales over time

 |
| **3** | Pie Chart | `/department-distribution-pie` | `[http://127.0.0.1:8000/department-distribution-pie](http://127.0.0.1:8000/department-distribution-pie)`<br> | Employee headcount breakdown by department

 |
| **4** | Scatter Plot | `/study-marks-scatter` | `[http://127.0.0.1:8000/study-marks-scatter](http://127.0.0.1:8000/study-marks-scatter)`<br> | Correlation between hours studied and exam scores (15 students)

 |
| **5** | Histogram | `/random-values-histogram` | `[http://127.0.0.1:8000/random-values-histogram](http://127.0.0.1:8000/random-values-histogram)`<br> | Frequency distribution of 500 NumPy-generated random values

 |
| **6** | Box Plot | `/employee-salary-box` | `[http://127.0.0.1:8000/employee-salary-box](http://127.0.0.1:8000/employee-salary-box)`<br> | Salary distribution, median, and IQR across 30 employees

 |
| **7** | Grouped Bar Chart | `/product-sales-grouped-bar` | `[http://127.0.0.1:8000/product-sales-grouped-bar](http://127.0.0.1:8000/product-sales-grouped-bar)`<br> | Multi-product comparison: Laptop, Mobile, and Tablet across 6 months

 |
| **8** | Grouped Bar Chart | `/student-performance-bar` | `[http://127.0.0.1:8000/student-performance-bar](http://127.0.0.1:8000/student-performance-bar)`<br> | Comparative marks for 10 students across Python, Mathematics, and Data Science

 |
| **9** | 3D Scatter Plot | `/age-salary-scatter3d` | `[http://127.0.0.1:8000/age-salary-scatter3d](http://127.0.0.1:8000/age-salary-scatter3d)`<br> | 3D multi-variable visualization for Age, Experience, and Salary

 |
| **10** | Funnel Chart | `/conversion-funnel` | `[http://127.0.0.1:8000/conversion-funnel](http://127.0.0.1:8000/conversion-funnel)`<br> | User attrition across marketing conversion stages

 |
| **11** | Line Plot | `/numpy-random-line` | `[http://127.0.0.1:8000/numpy-random-line](http://127.0.0.1:8000/numpy-random-line)` | Sequential plot mapping 100 NumPy random values

 |
| **12** | Subplot Dashboard | `/company-dashboard` | `[http://127.0.0.1:8000/company-dashboard](http://127.0.0.1:8000/company-dashboard)`<br> | 2x2 multi-metric dashboard: Revenue, Expenses, Employees, Customers

 |

---