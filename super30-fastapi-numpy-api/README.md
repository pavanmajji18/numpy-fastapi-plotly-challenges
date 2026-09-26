# ⚡ Super30 FastAPI & NumPy Numerical Analysis API

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.100%2B-009688.svg)](https://fastapi.tiangolo.com/)
[![NumPy](https://img.shields.io/badge/NumPy-1.24%2B-013243.svg)](https://numpy.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

A high-performance numerical analysis microservice combining **FastAPI**'s asynchronous web framework with **NumPy**'s vectorized C-accelerated array computing. This RESTful API exposes dynamic endpoints for statistical evaluations, array transformations, boolean masking, and dynamic mathematical calculations.

---

## 📌 Features

- 🚀 **Asynchronous REST Microservice**: Built with FastAPI for high throughput and ultra-low latency.
- 🧮 **Vectorized Computation**: Leverages NumPy array operations (`np.arange`, vector multiplication) instead of traditional Python loops for computational speed.
- 📊 **Statistical Analysis Engine**: Exposes dynamic dynamic calculations for Mean, Median, Standard Deviation, Variance, Min/Max, and Total Sum.
- 🔍 **Boolean Index Masking**: Filters data dynamically (e.g., dynamic dynamic even/odd splits) using NumPy array masking algorithms.
- 🔒 **JSON Serialization Safety**: Handles raw NumPy C-types (`int64`, `float64`) via explicit native type-casting (`int()`, `float()`, `.tolist()`) for seamless REST JSON responses.
- 📖 **Self-Documenting Spec**: Automated interactive Swagger UI (`/docs`) and ReDoc (`/redoc`).

---

## 🛠️ Tech Stack

- **Language:** Python 3.10+
- **Framework:** FastAPI
- **Numerical Library:** NumPy
- **ASGI Server:** Uvicorn

---

## 📁 Project Structure

```text
super30-fastapi-numpy-api/
├── main.py              # FastAPI routes, NumPy calculation logic & serialization
├── requirements.txt     # Python dependency specifications
└── README.md            # Project technical documentation
```

---

## 🚀 Quick Start & Setup

### 1. Prerequisites
- Python 3.10 or higher
- `pip` package manager

### 2. Clone Repository & Setup Virtual Environment
```bash
git clone <repository-url>
cd super30-fastapi-numpy-api
```

**Windows (PowerShell):**
```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

**macOS / Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run Application
```bash
uvicorn main:app --reload
```
Access the application at `http://127.0.0.1:8000`.

---

## 📖 API Reference

Access interactive documentation at:
- **Swagger UI:** [`http://127.0.0.1:8000/docs`](http://127.0.0.1:8000/docs)
- **ReDoc:** [`http://127.0.0.1:8000/redoc`](http://127.0.0.1:8000/redoc)

### Available Endpoints

| Method | Endpoint | Description | Sample Output |
| :--- | :--- | :--- | :--- |
| `GET` | `/numbers` | Fetch raw underlying array | `{"numbers": [12, 15, ...]}` |
| `GET` | `/mean` | Compute arithmetic mean | `{"mean": 48.25}` |
| `GET` | `/median` | Compute median value | `{"median": 38.0}` |
| `GET` | `/std` | Standard deviation | `{"standard_deviation": 31.42}` |
| `GET` | `/variance` | Statistical variance | `{"variance": 987.52}` |
| `GET` | `/maximum` | Dynamic maximum element | `{"maximum": 99}` |
| `GET` | `/minimum` | Dynamic minimum element | `{"minimum": 12}` |
| `GET` | `/sum` | Aggregate array sum | `{"sum": 579}` |
| `GET` | `/even` | Filter even elements (Boolean Masking) | `{"even_numbers": [12, 42, ...]}` |
| `GET` | `/odd` | Filter odd elements (Boolean Masking) | `{"odd_numbers": [15, 23, ...]}` |
| `GET` | `/stats` | Complete statistical metrics payload | `{"mean": 48.25, ...}` |
| `GET` | `/table/{number}` | Vectorized multiplication table calculation | `{"number": 7, "results": [...]}` |

---

## 💡 Key Engineering Considerations

1. **Performance via Vectorization**: Replaced conventional iterative `for` loops with vectorized NumPy arrays (`np.arange`), shifting loop execution down to C-speed memory buffers.
2. **Memory-efficient Boolean Indexing**: Utilized boolean index arrays (`data % 2 == 0`) for continuous memory filtering instead of standard Python list comprehensions.
3. **JSON Serialization Guard**: Solved NumPy's native `TypeError: Object of type int64 is not JSON serializable` by cleanly mapping output scalars and arrays to native Python types prior to endpoint return.

---

## 👤 Author

**Pavan Kumar Majji** 

