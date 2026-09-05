from fastapi import FastAPI
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

app = FastAPI(title="Super30 Plotly Visualization Challenge")


# 1. Bar Chart: Monthly Sales
@app.get("/monthly-sales-bar")
def monthly_sales_bar():
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
    sales = [120, 150, 170, 140, 200, 230]
    df = pd.DataFrame({"Month": months, "Sales": sales})
    fig = px.bar(
        df,
        x="Month",
        y="Sales",
        title="Monthly Sales",
        labels={"Month": "Month", "Sales": "Sales"},
    )
    fig.show()
    return {"message": "Monthly Sales Bar Chart opened"}


# 2. Line Chart: Monthly Sales
@app.get("/monthly-sales-line")
def monthly_sales_line():
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
    sales = [120, 150, 170, 140, 200, 230]
    df = pd.DataFrame({"Month": months, "Sales": sales})
    fig = px.line(
        df,
        x="Month",
        y="Sales",
        markers=True,
        title="Monthly Sales Line Chart",
        labels={"Month": "Month", "Sales": "Sales"},
    )
    fig.show()
    return {"message": "Monthly Sales Line Chart opened"}


# 3. Pie Chart: Department-wise Employee Distribution
@app.get("/department-distribution-pie")
def department_distribution_pie():
    df = pd.DataFrame(
        {
            "Department": ["Engineering", "Sales", "Marketing", "HR", "Operations"],
            "Employees": [40, 25, 15, 10, 10],
        }
    )
    fig = px.pie(
        df,
        names="Department",
        values="Employees",
        title="Department-wise Employee Distribution",
    )
    fig.show()
    return {"message": "Department Distribution Pie Chart opened"}


# 4. Scatter Plot: Hours Studied vs Exam Marks
@app.get("/study-marks-scatter")
def study_marks_scatter():
    df = pd.DataFrame(
        {
            "Hours": [2, 3, 4, 5, 5.5, 6, 6.5, 7, 7.5, 8, 8.5, 9, 9.5, 10, 11],
            "Marks": [35, 42, 50, 55, 60, 68, 70, 75, 74, 82, 85, 88, 91, 95, 98],
        }
    )
    fig = px.scatter(
        df,
        x="Hours",
        y="Marks",
        title="Hours Studied vs Exam Marks",
        labels={"Hours": "Hours Studied", "Marks": "Exam Marks"},
    )
    fig.show()
    return {"message": "Study vs Marks Scatter Plot opened"}


# 5. Histogram: 500 Random Values
@app.get("/random-values-histogram")
def random_values_histogram():
    values = np.random.randn(500)
    df = pd.DataFrame({"Values": values})
    fig = px.histogram(
        df,
        x="Values",
        title="Histogram of 500 Random Values",
        labels={"Values": "Random Values"},
    )
    fig.show()
    return {"message": "500 Values Histogram opened"}


# 6. Box Plot: Employee Salaries
@app.get("/employee-salary-box")
def employee_salary_box():
    salaries = [
        35000, 38000, 42000, 45000, 48000, 50000, 52000, 53000, 55000, 56000,
        58000, 60000, 62000, 64000, 65000, 67000, 69000, 71000, 72000, 75000,
        78000, 80000, 82000, 85000, 88000, 90000, 95000, 98000, 105000, 120000,
    ]
    df = pd.DataFrame({"Salary": salaries})
    fig = px.box(
        df,
        y="Salary",
        points="all",
        title="Employee Salary Distribution",
        labels={"Salary": "Salary in USD"},
    )
    fig.show()
    return {"message": "Salary Distribution Box Plot opened"}


# 7. Grouped Bar Chart: Laptop, Mobile, Tablet Sales
@app.get("/product-sales-grouped-bar")
def product_sales_grouped_bar():
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"] * 3
    products = ["Laptop"] * 6 + ["Mobile"] * 6 + ["Tablet"] * 6
    units = [
        120, 130, 150, 140, 180, 210,
        200, 220, 250, 240, 290, 310,
        80, 90, 85, 100, 110, 125,
    ]
    df = pd.DataFrame({"Month": months, "Product": products, "Sales": units})
    fig = px.bar(
        df,
        x="Month",
        y="Sales",
        color="Product",
        barmode="group",
        title="Sales Comparison of Laptop, Mobile, and Tablet",
        labels={"Month": "Month", "Sales": "Units Sold", "Product": "Product Category"},
    )
    fig.show()
    return {"message": "Product Sales Grouped Bar Chart opened"}


# 8. Grouped Bar Chart: Student Performance
@app.get("/student-performance-bar")
def student_performance_bar():
    students = [f"Student {i+1}" for i in range(10)]
    df = pd.DataFrame(
        {
            "Student": students,
            "Python": [85, 78, 92, 65, 88, 95, 70, 82, 77, 90],
            "Mathematics": [80, 85, 89, 60, 82, 91, 75, 88, 80, 85],
            "Data Science": [88, 82, 95, 72, 85, 98, 68, 86, 82, 94],
        }
    )
    df_melted = df.melt(
        id_vars=["Student"],
        value_vars=["Python", "Mathematics", "Data Science"],
        var_name="Subject",
        value_name="Marks",
    )
    fig = px.bar(
        df_melted,
        x="Student",
        y="Marks",
        color="Subject",
        barmode="group",
        title="Student Performance in Python, Mathematics, and Data Science",
        labels={"Student": "Student", "Marks": "Marks", "Subject": "Subject"},
    )
    fig.show()
    return {"message": "Student Performance Chart opened"}


# 9. 3D Scatter Plot: Age, Salary, Experience
@app.get("/age-salary-scatter3d")
def age_salary_scatter3d():
    age = np.random.randint(22, 50, size=30)
    experience = np.maximum(0, age - 22 + np.random.randint(-1, 2, size=30))
    salary = 30000 + experience * 4000 + np.random.randint(1000, 5000, size=30)

    df = pd.DataFrame({"Age": age, "Experience": experience, "Salary": salary})
    fig = px.scatter_3d(
        df,
        x="Age",
        y="Experience",
        z="Salary",
        color="Salary",
        title="3D Scatter Plot: Age, Salary, Experience",
        labels={"Age": "Age", "Experience": "Experience", "Salary": "Salary"},
    )
    fig.show()
    return {"message": "3D Scatter Plot opened"}


# 10. Funnel Chart: Custom Graph
@app.get("/conversion-funnel")
def conversion_funnel():
    df = pd.DataFrame(
        {
            "Stage": ["Website Visitors", "Signups", "Trial", "Paid"],
            "Users": [10000, 4000, 1500, 600],
        }
    )
    fig = px.funnel(
        df,
        x="Users",
        y="Stage",
        title="Funnel Chart - Conversion Stages",
        labels={"Users": "User Count", "Stage": "Funnel Stage"},
    )
    fig.show()
    return {"message": "Conversion Funnel Chart opened"}


# 11. Line Plot: 100 Random Numbers with NumPy
@app.get("/numpy-random-line")
def numpy_random_line():
    data = np.random.rand(100)
    df = pd.DataFrame({"Index": np.arange(1, 101), "Value": data})
    fig = px.line(
        df,
        x="Index",
        y="Value",
        markers=True,
        title="100 Random Numbers with NumPy and Plotly",
        labels={"Index": "Index", "Value": "Random Value"},
    )
    fig.show()
    return {"message": "NumPy Random Line Plot opened"}


# 12. Dashboard Thinking Challenge
@app.get("/company-dashboard")
def company_dashboard():
    quarters = ["Q1", "Q2", "Q3", "Q4"]
    revenue = [120000, 150000, 180000, 220000]
    expenses = [80000, 95000, 100000, 125000]
    employees = [30, 42, 55, 65]
    customers = [800, 1200, 1700, 2400]

    fig = make_subplots(
        rows=2,
        cols=2,
        subplot_titles=(
            "Revenue",
            "Expenses",
            "Employees",
            "Customers",
        ),
    )

    fig.add_trace(go.Bar(x=quarters, y=revenue, name="Revenue"), row=1, col=1)
    fig.add_trace(go.Bar(x=quarters, y=expenses, name="Expenses"), row=1, col=2)
    fig.add_trace(go.Scatter(x=quarters, y=employees, mode="lines+markers", name="Employees"), row=2, col=1)
    fig.add_trace(go.Scatter(x=quarters, y=customers, mode="lines+markers", name="Customers"), row=2, col=2)

    fig.update_layout(title_text="Fictional Company Dashboard", showlegend=False)
    fig.show()
    return {"message": "Company Dashboard opened"}