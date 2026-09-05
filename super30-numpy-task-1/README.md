# Super30: NumPy Data Analysis Challenge

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![NumPy](https://img.shields.io/badge/Library-NumPy-013243.svg?logo=numpy)](https://numpy.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

A hands-on implementation of core vectorization, array manipulation, conditional filtering, linear algebra, and statistical operations using Python's fundamental scientific computing library: **NumPy**.

---

## 📌 Repository Structure

```text
super30-numpy-task-1/
├── requirements.txt      # Project dependencies
├── main.py               # Complete implementation of Problems 1–12
└── README.md             # Project documentation & output walkthrough

```

---

## 🚀 Quickstart & Execution

### 1. Clone the repository

```bash
git clone [https://github.com/](https://github.com/)<your-username>/super30-numpy-task-1.git
cd super30-numpy-task-1

```

### 2. Set up a virtual environment (Recommended)

```bash
python -m venv venv
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

```

### 3. Install dependencies

```bash
pip install -r requirements.txt

```

### 4. Execute the suite

```bash
python main.py

```

---

## 🧠 Concepts & Problem Breakdown

| # | Challenge Module | Key NumPy Concepts Applied | Methods & Operators Used |
| --- | --- | --- | --- |
| **1** | Array Creation | Step ranges, sequence generation | `np.arange(start, stop, step)` |
| **2** | Student Marks Analysis | Descriptive statistics & aggregation | `np.sum`, `np.mean`, `np.median`, `np.min`, `np.max` |
| **3** | Filtering | Boolean masking & conditional selection | `arr[condition]`, `marks[marks > threshold]` |
| **4** | Reshaping | Dimensional transformation without data copy | `.reshape(rows, cols)` |
| **5** | 2D Array Manipulation | Row/column coordinate slicing | `arr[row, :]`, `arr[:, col]`, `arr[r, c]` |
| **6** | Arithmetic Operations | Element-wise vectorized computing | `+`, `-`, `*`, `/` |
| **7** | Statistical Analysis | Normal distribution sampling & variance | `np.random.normal()`, `np.std()`, `np.var()` |
| **8** | Sorting | In-place sorting and slice reversing | `np.sort()`, `[::-1]` |
| **9** | Unique Values | Set identification and deduplication | `np.unique()` |
| **10** | Matrix Operations | Hadamard product vs. dot product | `*` (element-wise), `@` (dot product) |
| **11** | Salary Analysis | Vectorized statistical thresholding | `np.mean()`, conditional masking |
| **12** | Matrix Aggregations | Multi-axis reductions on 2D random matrices | `axis=0` (cols), `axis=1` (rows) |

---

## 📋 Detailed Solutions & Output Walkthrough

### Problem 1: Array Creation

Generates integer sequences using `np.arange(start, stop, step)`. The `stop` value is exclusive.

* **1 to 50:** `np.arange(1, 51)`
* **Evens (2 to 100):** `np.arange(2, 101, 2)`
* **Odds (1 to 99):** `np.arange(1, 100, 2)`

### Problem 2 & 3: Student Marks Analysis & Filtering

Evaluates scores: `[78, 85, 92, 67, 88, 73, 95, 60, 84, 91]`

* **Total:** `813` | **Average:** `81.3` | **Median:** `84.5`
* **High / Low:** `95` / `60`
* **Boolean Masks:**
* Above 90: `[92, 95, 91]`
* Above Average (> 81.3): `[85, 92, 88, 95, 84, 91]`
* Below 70: `[67, 60]`



### Problem 4 & 5: Reshaping & Slicing

* **Reshape:** A continuous 1D block of 20 elements is mapped to shape `(4, 5)` while preserving element count ($4 \times 5 = 20$).
* **2D Slicing:**
```python
matrix = np.array([[10, 20, 30],
                   [40, 50, 60],
                   [70, 80, 90]])

```


* Row 0: `matrix[0, :]` $\rightarrow$ `[10, 20, 30]`
* Column 1: `matrix[:, 1]` $\rightarrow$ `[20, 50, 80]`
* Item (1, 2): `matrix[1, 2]` $\rightarrow$ `60`



### Problem 6 & 10: Mathematical & Matrix Operations

Differentiates between element-wise arithmetic and linear algebra:

* **Hadamard Product (`*`):** Multiplies corresponding indices element-by-element.
* **Matrix Product (`@`):** Performs standard matrix multiplication ($C_{ij} = \sum_k A_{ik} B_{kj}$).

### Problem 7: Statistical Analysis

Samples 100 values from standard normal distribution ($\mu=0, \sigma=1$):

* Standard deviation computed with `np.std(data)`
* Population variance verified using `np.var(data) == np.std(data)**2`

### Problem 8 & 9: Sorting and Set Operations

* **Ascending:** `np.sort(arr)`
* **Descending:** `np.sort(arr)[::-1]` (step slice by -1)
* **Unique Elements:** `np.unique([1, 2, 2, 3, 3, 3, 4, 5, 5, 6])` yields `[1, 2, 3, 4, 5, 6]`

### Problem 11 & 12: Salary Analysis & Matrix Challenge

* Computes salary thresholds using vector masks: `salaries[salaries > np.mean(salaries)]`.
* Multi-axis reductions on a $5 \times 5$ random matrix:
* `axis=0`: Collapses rows downward to return **column sums** (length 5 array).
* `axis=1`: Collapses columns across to return **row sums** (length 5 array).