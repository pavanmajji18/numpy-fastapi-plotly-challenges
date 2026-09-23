# Super30: FastAPI GET API Suite

![Python Version](https://img.shields.io/badge/Python-3.8%2B-blue.svg?style=for-the-badge&logo=python)
![FastAPI](https://img.shields.io/badge/Framework-FastAPI-009688.svg?style=for-the-badge&logo=fastapi)
![Uvicorn](https://img.shields.io/badge/ASGI-Uvicorn-4051B5.svg?style=for-the-badge)
![OpenAPI](https://img.shields.io/badge/Documentation-Swagger%20%2F%20ReDoc-85EA2D.svg?style=for-the-badge&logo=openapi-initiative)
![License](https://img.shields.io/badge/License-MIT-green.svg?style=for-the-badge)

A high-performance backend API service built with **FastAPI** and **Uvicorn**, showcasing RESTful GET endpoint design, dynamic path parameter parsing, strict type validation, and automatic OpenAPI documentation.

---

## 🔗 Repository Links

- **GitHub Repository**: [FastAPI GET API Task](https://github.com/pavanmajji18/numpy-fastapi-plotly-challenges/tree/6450599bed3b93d029c874d6048994e2be5c8ff1/super30-fastapi-get-api-task)

---

## 📌 Table of Contents

- [Overview & Key Learnings](#-overview--key-learnings)
- [Repository Structure](#-repository-structure)
- [API Route Catalog](#-api-route-catalog)
- [Endpoint Specifications](#-endpoint-specifications)
- [Quickstart & Execution](#-quickstart--execution)
- [Interactive API Documentation](#-interactive-api-documentation)
- [Tech Stack](#-tech-stack)

---

## 🎯 Overview & Key Learnings

This project delivers a suite of 12 distinct RESTful GET APIs built to demonstrate foundational modern Python backend development skills:

- **Static & Dynamic Routing**: Designing clean API endpoints for static payloads and dynamic parameter-driven queries.
- **Automatic Type Validation**: Harnessing Python type hints for runtime parameter parsing, conversion, and auto-generated 422 Unprocessable Entity responses for bad inputs.
- **RESTful Response Standards**: Structuring clean, serializable JSON responses.
- **Interactive Documentation**: Auto-generating live OpenAPI/Swagger UI and ReDoc documentation out of the box.

---

## 📂 Repository Structure

```text
super30-fastapi-get-api-task/
├── main.py               # Complete FastAPI application with 12 endpoints
├── requirements.txt      # Dependencies (fastapi, uvicorn)
└── README.md             # Project documentation
```

---

## 🛠️ API Route Catalog

| # | Endpoint Method & Path | Query / Path Parameters | Description |
|---|---|---|---|
| **01** | `GET /` | None | Welcome greeting endpoint |
| **02** | `GET /student` | None | Static student metadata payload |
| **03** | `GET /course` | None | Course curriculum & topic details |
| **04** | `GET /skills` | None | Backend technology skills listing |
| **05** | `GET /add/{num1}/{num2}` | `num1: int`, `num2: int` | Addition of two integer path parameters |
| **06** | `GET /multiply/{num1}/{num2}` | `num1: int`, `num2: int` | Multiplication of two integer path parameters |
| **07** | `GET /square/{number}` | `number: int` | Calculates the square of a number |
| **08** | `GET /check/{number}` | `number: int` | Parity checker (Even vs. Odd) |
| **09** | `GET /age/{age}` | `age: int` | Age classification (Child, Teenager, Adult, Senior) |
| **10** | `GET /table/{number}` | `number: int` | Generates a 1-to-10 multiplication table |
| **11** | `GET /profile/{name}/{age}` | `name: str`, `age: int` | Dynamic user profile generator |
| **12** | `GET /number/{number}` | `number: int` | Complete numerical analysis (Square, Cube, Parity) |

---

## 📖 Endpoint Specifications

### 1. Basic & Static Data Endpoints

- **`GET /`**
  ```json
  { "message": "Welcome to Super30 FastAPI" }
  ```

- **`GET /student`**
  ```json
  {
    "name": "Pavan",
    "batch": "Super30-July-2026",
    "role": "Student"
  }
  ```

- **`GET /course`**
  ```json
  {
    "course_name": "Backend Development with FastAPI",
    "mentor": "Sudhanshu",
    "duration": "8 Weeks",
    "topics": ["Python", "FastAPI", "REST API", "Database", "Deployment"]
  }
  ```

- **`GET /skills`**
  ```json
  { "skills": ["Python", "FastAPI", "SQL", "Docker", "AWS"] }
  ```

### 2. Math & Calculation Endpoints

- **`GET /add/15/25`** $\rightarrow$ `{ "result": 40 }`
- **`GET /multiply/7/6`** $\rightarrow$ `{ "result": 42 }`
- **`GET /square/9`** $\rightarrow$ `{ "number": 9, "square": 81 }`

### 3. Logic & Classification Endpoints

- **`GET /check/14`**
  ```json
  { "number": 14, "type": "even" }
  ```

- **`GET /age/24`**
  ```json
  { "age": 24, "message": "You are an adult." }
  ```

- **`GET /table/5`**
  ```json
  {
    "number": 5,
    "table": [
      "5 x 1 = 5", "5 x 2 = 10", "5 x 3 = 15", "5 x 4 = 20", "5 x 5 = 25",
      "5 x 6 = 30", "5 x 7 = 35", "5 x 8 = 40", "5 x 9 = 45", "5 x 10 = 50"
    ]
  }
  ```

- **`GET /profile/Pavan/24`**
  ```json
  { "name": "Pavan", "age": 24 }
  ```

- **`GET /number/7`**
  ```json
  {
    "number": 7,
    "square": 49,
    "cube": 343,
    "even": false
  }
  ```

---

## 🚀 Quickstart & Execution

### Prerequisites
- Python 3.8+ installed.

### Step-by-Step Setup

1. **Clone the Repository**
   ```bash
   git clone https://github.com/pavanmajji18/numpy-fastapi-plotly-challenges.git
   cd numpy-fastapi-plotly-challenges/super30-fastapi-get-api-task
   ```

2. **Create & Activate Virtual Environment**
   - **Windows:**
     ```bash
     python -m venv venv
     venv\Scripts\activate
     ```
   - **macOS / Linux:**
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Launch the Server**
   ```bash
   uvicorn main:app --reload
   ```

5. **Access the API**
   - API Base URL: `http://127.0.0.1:8000`

---

## 🌐 Interactive API Documentation

FastAPI automatically parses endpoint signatures and generates interactive OpenAPI schemas:

- **Swagger UI**: Visit [`http://127.0.0.1:8000/docs`](http://127.0.0.1:8000/docs) to test endpoints interactively from your browser.
- **ReDoc UI**: Visit [`http://127.0.0.1:8000/redoc`](http://127.0.0.1:8000/redoc) for clean, publication-ready API documentation.

---

## 💻 Tech Stack

- **Language**: Python 3.8+
- **Framework**: [FastAPI](https://fastapi.tiangolo.com/)
- **ASGI Server**: [Uvicorn](https://www.uvicorn.org/)
- **Specification**: OpenAPI (Swagger UI / ReDoc)
