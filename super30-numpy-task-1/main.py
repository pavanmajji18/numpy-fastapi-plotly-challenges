import numpy as np

# ==========================================
# Problem 1: Array Creation
# ==========================================
print("--- Problem 1: Array Creation ---")
nums_1_to_50 = np.arange(1, 51)
evens_2_to_100 = np.arange(2, 101, 2)
odds_1_to_99 = np.arange(1, 100, 2)

print("Numbers 1-50:\n", nums_1_to_50)
print("Even numbers 2-100:\n", evens_2_to_100)
print("Odd numbers 1-99:\n", odds_1_to_99)


# ==========================================
# Problem 2: Student Marks Analysis
# ==========================================
print("\n--- Problem 2: Student Marks Analysis ---")
marks = np.array([78, 85, 92, 67, 88, 73, 95, 60, 84, 91])

total_marks = np.sum(marks)
avg_marks = np.mean(marks)
max_marks = np.max(marks)
min_marks = np.min(marks)
median_marks = np.median(marks)

print("Marks:", marks)
print("Total:", total_marks)
print("Average:", avg_marks)
print("Maximum:", max_marks)
print("Minimum:", min_marks)
print("Median:", median_marks)


# ==========================================
# Problem 3: Filtering
# ==========================================
print("\n--- Problem 3: Filtering ---")
above_90 = marks[marks > 90]
above_avg = marks[marks > np.mean(marks)]
below_70 = marks[marks < 70]

print("Marks above 90:", above_90)
print("Marks above average:", above_avg)
print("Marks below 70:", below_70)


# ==========================================
# Problem 4: Reshaping
# ==========================================
print("\n--- Problem 4: Reshaping ---")
arr_20 = np.arange(1, 21)
reshaped_4x5 = arr_20.reshape((4, 5))

print("Original 1D array:", arr_20)
print("Reshaped 4x5 array:\n", reshaped_4x5)


# ==========================================
# Problem 5: Two-Dimensional Array
# ==========================================
print("\n--- Problem 5: Two-Dimensional Array ---")
matrix_3x3 = np.array([[10, 20, 30], [40, 50, 60], [70, 80, 90]])

first_row = matrix_3x3[0, :]
second_col = matrix_3x3[:, 1]
elem_1_2 = matrix_3x3[1, 2]

print("Matrix:\n", matrix_3x3)
print("Row 0 selection:", first_row)
print("Column 1 selection:", second_col)
print("Element at row 1, col 2:", elem_1_2)


# ==========================================
# Problem 6: Mathematical Operations
# ==========================================
print("\n--- Problem 6: Mathematical Operations ---")
a = np.array([10, 20, 30, 40, 50])
b = np.array([5, 10, 15, 20, 25])

add_res = a + b
sub_res = a - b
mul_res = a * b
div_res = a / b

print("a:", a)
print("b:", b)
print("Addition:", add_res)
print("Subtraction:", sub_res)
print("Multiplication:", mul_res)
print("Division:", div_res)


# ==========================================
# Problem 7: Statistical Analysis
# ==========================================
print("\n--- Problem 7: Statistical Analysis ---")
rand_100 = np.random.normal(0, 1, 100)

mean_val = np.mean(rand_100)
median_val = np.median(rand_100)
std_dev = np.std(rand_100)
variance = np.var(rand_100)

print("Mean:", mean_val)
print("Median:", median_val)
print("Standard Deviation:", std_dev)
print("Variance:", variance)


# ==========================================
# Problem 8: Sorting
# ==========================================
print("\n--- Problem 8: Sorting ---")
unsorted_arr = np.array([45, 12, 89, 23, 7, 67, 34])
ascending = np.sort(unsorted_arr)
descending = ascending[::-1]

print("Original array:", unsorted_arr)
print("Ascending sort:", ascending)
print("Descending sort:", descending)


# ==========================================
# Problem 9: Unique Values
# ==========================================
print("\n--- Problem 9: Unique Values ---")
dup_arr = np.array([1, 2, 2, 3, 3, 3, 4, 5, 5, 6])
unique_vals = np.unique(dup_arr)

print("Original array:", dup_arr)
print("Unique values:", unique_vals)


# ==========================================
# Problem 10: Matrix Operations
# ==========================================
print("\n--- Problem 10: Matrix Operations ---")
mat_a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
mat_b = np.array([[9, 8, 7], [6, 5, 4], [3, 2, 1]])

mat_add = mat_a + mat_b
mat_sub = mat_a - mat_b
mat_elem_mul = mat_a * mat_b
mat_dot = mat_a @ mat_b

print("Matrix A:\n", mat_a)
print("Matrix B:\n", mat_b)
print("Addition:\n", mat_add)
print("Subtraction:\n", mat_sub)
print("Element-wise Multiplication:\n", mat_elem_mul)
print("Matrix Multiplication (@):\n", mat_dot)


# ==========================================
# Problem 11: Salary Analysis
# ==========================================
print("\n--- Problem 11: Salary Analysis ---")
salaries = np.array(
    [
        45000,
        52000,
        61000,
        39000,
        72000,
        48000,
        55000,
        67000,
        80000,
        43000,
        59000,
        64000,
        71000,
        38000,
        50000,
    ]
)

max_salary = np.max(salaries)
min_salary = np.min(salaries)
avg_salary = np.mean(salaries)
above_avg_salaries = salaries[salaries > avg_salary]

print("Salaries:", salaries)
print("Highest Salary:", max_salary)
print("Lowest Salary:", min_salary)
print("Average Salary:", avg_salary)
print("Salaries Above Average:", above_avg_salaries)


# ==========================================
# Problem 12: Challenge
# ==========================================
print("\n--- Problem 12: Challenge ---")
rand_5x5 = np.random.randint(1, 100, (5, 5))

grid_max = np.max(rand_5x5)
grid_min = np.min(rand_5x5)
row_sums = np.sum(rand_5x5, axis=1)
col_sums = np.sum(rand_5x5, axis=0)
grid_avg = np.mean(rand_5x5)

print("5x5 Random Matrix:\n", rand_5x5)
print("Maximum Value:", grid_max)
print("Minimum Value:", grid_min)
print("Row-wise Sums:", row_sums)
print("Column-wise Sums:", col_sums)
print("Overall Average:", grid_avg)