# Super30: NumPy Data Analysis & Vectorized Scientific Computing

![Python Version](https://img.shields.io/badge/Python-3.8%2B-blue.svg?style=for-the-badge&logo=python)
![NumPy](https://img.shields.io/badge/Library-NumPy-013243.svg?style=for-the-badge&logo=numpy)
![License](https://img.shields.io/badge/License-MIT-green.svg?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Completed-success.svg?style=for-the-badge)

A comprehensive, hands-on implementation of high-performance scientific computing and data analysis techniques using Python's core numerical computing library, **NumPy**. This repository demonstrates vectorization, multi-dimensional array manipulation, boolean filtering, statistical modeling, and linear algebra.

---

## 🔗 Repository Links

- **GitHub Repository**: [NumPy Data Analysis Challenge](https://github.com/pavanmajji18/numpy-fastapi-plotly-challenges/tree/6450599bed3b93d029c874d6048994e2be5c8ff1/super30-numpy-task-1)

---

## 📌 Table of Contents

- [Overview & Objectives](#-overview--objectives)
- [Repository Structure](#-repository-structure)
- [Key Features & Modules](#-key-features--modules)
- [Problem-by-Problem Breakdown](#-problem-by-problem-breakdown)
- [Getting Started & Execution](#-getting-started--execution)
- [Sample Output & Results](#-sample-output--results)
- [Tech Stack](#-tech-stack)

---

## 🎯 Overview & Objectives

The goal of this project is to eliminate inefficient Python loops by leveraging vectorized operations and C-accelerated array computing in **NumPy**. Across 12 distinct challenge modules, this project covers:

- Efficient numerical sequence generation and step-range creation.
- Statistical data analytics (descriptive statistics, distribution sampling, variance).
- Complex boolean logic and array filtering without branching loops.
- Multi-dimensional matrix transformations, slicing, and axis-wise reductions.
- Linear algebra operations (Hadamard element-wise product vs. matrix dot product).

---

## 📂 Repository Structure

```text
super30-numpy-task-1/
├── main.py               # Executable script solving Problems 1 to 12
├── output.txt            # Captured console output of all solutions
├── requirements.txt      # Project dependency list (numpy)
└── README.md             # Project documentation
```

---

## 🛠️ Key Features & Modules

| # | Module | Core Concept | Key Methods & Operators |
|---|---|---|---|
| **01** | Array Creation | Range generation & sequence bounds | `np.arange(start, stop, step)` |
| **02** | Student Marks Analysis | Summary statistics & aggregations | `np.sum`, `np.mean`, `np.median`, `np.min`, `np.max` |
| **03** | Conditional Filtering | Vectorized boolean masking | `arr[condition]`, `marks[marks > threshold]` |
| **04** | Array Reshaping | Dimensional transformation | `.reshape(rows, cols)` |
| **05** | 2D Slicing & Subsetting | Row/column indexing | `arr[row, :]`, `arr[:, col]`, `arr[r, c]` |
| **06** | Vectorized Arithmetic | Element-wise mathematics | `+`, `-`, `*`, `/` |
| **07** | Statistical Modeling | Normal distribution & variance | `np.random.normal()`, `np.std()`, `np.var()` |
| **08** | Array Sorting | Ascending/Descending ordering | `np.sort()`, `[::-1]` |
| **09** | Deduplication | Set identification & unique values | `np.unique()` |
| **10** | Linear Algebra | Hadamard product vs Dot product | `*` (element-wise), `@` (dot product) |
| **11** | Real-World Salary Analysis | Data analytics & thresholding | `salaries[salaries > np.mean(salaries)]` |
| **12** | Matrix Aggregations | Multi-axis reductions on 5x5 matrix | `axis=0` (columns), `axis=1` (rows) |

---

## 🧠 Problem-by-Problem Breakdown

### 1. Array Creation (`np.arange`)
Generates 1D arrays over specified intervals:
- **Numbers 1–50**: `np.arange(1, 51)`
- **Evens 2–100**: `np.arange(2, 101, 2)`
- **Odds 1–99**: `np.arange(1, 100, 2)`

### 2 & 3. Student Marks Analysis & Filtering
Analyzes a score dataset: `[78, 85, 92, 67, 88, 73, 95, 60, 84, 91]`
- Computes aggregate metrics: Total (`813`), Mean (`81.3`), Median (`84.5`), Min (`60`), Max (`95`).
- Applies boolean masks:
  - Distinctions (> 90): `[92, 95, 91]`
  - Above Average (> 81.3): `[85, 92, 88, 95, 84, 91]`
  - Remedial (< 70): `[67, 60]`

### 4 & 5. Reshaping & 2D Slicing
- Transforms a 20-element 1D array into a `(4, 5)` matrix.
- Extracts specific rows, columns, and elements from a $3 \times 3$ grid using zero-based slicing (`[row, col]`).

### 6 & 10. Vectorized Math & Matrix Multiplication
- Compares element-wise operators (`+`, `-`, `*`, `/`) with matrix dot products.
- Demonstrates difference between Hadamard product (`A * B`) and matrix multiplication (`A @ B`).

### 7. Normal Distribution & Statistical Measures
- Generates 100 random values from Gaussian distribution $\mathcal{N}(\mu=0, \sigma=1)$.
- Calculates Mean, Median, Standard Deviation, and Variance.

### 8 & 9. Sorting & Unique Elements
- Sorts arrays in ascending order using `np.sort()` and descending order using index slicing `[::-1]`.
- Deduplicates raw arrays containing repeated integers with `np.unique()`.

### 11 & 12. Real-World Analytics & Matrix Aggregation Challenge
- Filters employee salaries above the calculated mean.
- Performs axis-specific reduction on a $5 \times 5$ random matrix:
  - `axis=0`: Column-wise summation (collapses rows).
  - `axis=1`: Row-wise summation (collapses columns).

---

## 🚀 Getting Started & Execution

### Prerequisites
- Python 3.8 or higher installed on your system.

### Setup Instructions

1. **Clone the Repository**
   ```bash
   git clone https://github.com/pavanmajji18/numpy-fastapi-plotly-challenges.git
   cd numpy-fastapi-plotly-challenges/super30-numpy-task-1
   ```

2. **Create and Activate a Virtual Environment**
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

4. **Run the Script**
   ```bash
   python main.py
   ```

---

## 📊 Sample Output & Results

Running `main.py` generates the following structured console output:

```text
--- Problem 1: Array Creation ---
Numbers 1-50:
 [ 1  2  3 ... 48 49 50]
Even numbers 2-100:
 [  2   4   6 ...  96  98 100]
Odd numbers 1-99:
 [ 1  3  5 ... 95 97 99]

--- Problem 2: Student Marks Analysis ---
Total: 813 | Average: 81.3 | Maximum: 95 | Minimum: 60 | Median: 84.5

--- Problem 10: Matrix Operations ---
Matrix A @ Matrix B:
[[ 30  24  18]
 [ 84  69  54]
 [138 114  90]]
```

---

## 💻 Tech Stack

- **Language**: Python 3.8+
- **Primary Library**: [NumPy](https://numpy.org/)
