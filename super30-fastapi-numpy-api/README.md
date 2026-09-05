# Super30 FastAPI & NumPy Calculation API

A high-performance numerical analysis microservice built with **FastAPI** and **NumPy**. This API exposes RESTful `GET` endpoints to dynamically perform statistical evaluations, boolean masking, and vectorized matrix calculations on numeric data without hard-coded outputs.

---

## Author
* **Student Name:** Pavan Kumar Majji

---

## Project Objective
The goal of this project is to integrate NumPy's vector processing capabilities into an asynchronous web API architecture using FastAPI. 

Key technical highlights:
* **Zero Hard-Coding:** All metrics are evaluated dynamically at runtime.
* **Vectorized Computing:** Multiplication tables and array splits are handled directly through NumPy vectorized arrays (`np.arange`) rather than standard Python loops.
* **Boolean Masking:** Conditional filtering (even/odd splits) leverages boolean index masks.
* **Native JSON Serialization:** Explicit type-casting (`int()`, `float()`, `.tolist()`) ensures raw NumPy C-types (`int64`, `float64`) serialize cleanly into standard JSON payloads.

---

## Project Structure

```text
super30-fastapi-numpy-api/
│
├── main.py              # FastAPI application, routing, and NumPy analysis logic
├── requirements.txt     # Application dependencies
└── README.md            # Documentation and setup guide