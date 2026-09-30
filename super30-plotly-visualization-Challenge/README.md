# Super30 Plotly Visualization Challenge

Convert raw data into meaningful, interactive data visualizations using **Plotly Express**, **Plotly Graph Objects**, **NumPy**, and **Pandas**, served seamlessly via **FastAPI** and **Swagger UI**.

---

## 👤 Author Information

* **Author:** Pavan Kumar Majji
* **Project:** super30-plotly-visualization-Challenge
* **LinkedIn:** [Pavan Kumar Majji](https://www.linkedin.com/in/pavan-kumar-majji-231303199/)
* **Repository:** [numpy-fastapi-plotly-challenges](https://github.com/pavanmajji18/numpy-fastapi-plotly-challenges/tree/main/super30-plotly-visualization-Challenge)

---

## 🚀 Key Features

* **⚡ API-Driven Visualizations:** Exposes 12 dedicated interactive visualization endpoints powered by FastAPI.
* **🌐 Interactive Swagger UI (`/docs`):** Test endpoints directly from the browser; executing an endpoint triggers Plotly's rendering engine (`fig.show()`) in a new browser tab.
* **📊 Comprehensive Visual Suite:** Covers 2D/3D Scatter Plots, Box Plots, Histograms, Funnel Charts, Grouped Bar Charts, Line Graphs, and Multi-Metric Dashboards.
* **🔧 Clean Modular Code:** Leverages Pandas DataFrames and NumPy array generators for robust data preparation.

---

## 📁 Repository Structure

```text
super30-plotly-visualization-Challenge/
├── main.py          # FastAPI application serving 12 Plotly visualization endpoints
├── requirements.txt # Project dependencies (fastapi, uvicorn, plotly, pandas, numpy)
└── README.md        # Project documentation
```

---

## 🛠️ Installation & Setup

1. **Clone or navigate to the repository directory:**
   ```bash
   cd super30-plotly-visualization-Challenge
   ```

2. **Create and activate a virtual environment (optional but recommended):**
   ```bash
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. **Install required dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

---

## 🚀 How to Run the Server

Start the FastAPI application using the Uvicorn ASGI server:

```bash
uvicorn main:app --reload --port 8000
```

Once the server is running, access the interactive Swagger UI in your browser:
👉 **Interactive API Documentation:** [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

> **How to execute:** From the Swagger UI interface, expand any endpoint, click **"Try it out"**, and press **"Execute"**. The endpoint triggers Plotly's interactive rendering engine and opens the visualization directly in a new browser tab.

---

## 📡 Available API Endpoints

| # | Chart Type | Endpoint Path | Description |
|---|---|---|---|
| **Doc** | Swagger UI | `/docs` | Interactive Swagger API testing console |
| **1** | Bar Chart | `/monthly-sales-bar` | Monthly sales for 6 months (`Jan` to `Jun`) |
| **2** | Line Chart | `/monthly-sales-line` | Trend view of monthly sales over time |
| **3** | Pie Chart | `/department-distribution-pie` | Employee headcount breakdown by department |
| **4** | Scatter Plot | `/study-marks-scatter` | Hours studied vs. exam scores correlation (15 students) |
| **5** | Histogram | `/random-values-histogram` | Frequency distribution of 500 NumPy random values |
| **6** | Box Plot | `/employee-salary-box` | Salary distribution, median, and IQR across 30 employees |
| **7** | Grouped Bar Chart | `/product-sales-grouped-bar` | Multi-product sales comparison across 6 months |
| **8** | Grouped Bar Chart | `/student-performance-bar` | Student performance across Python, Math, and Data Science |
| **9** | 3D Scatter Plot | `/age-salary-scatter3d` | 3D multi-variable plot mapping Age, Experience, and Salary |
| **10** | Funnel Chart | `/conversion-funnel` | User conversion stages and marketing attrition |
| **11** | Line Plot | `/numpy-random-line` | Sequential mapping of 100 NumPy random values |
| **12** | Subplot Dashboard | `/company-dashboard` | 2x2 multi-metric executive dashboard |

---

## 📜 License

This project is open-source and available under the [MIT License](LICENSE).
