from fastapi import FastAPI

app = FastAPI(
    title="Super30 FastAPI GET API Assignment",
    description="A collection of 12 GET APIs demonstrating path parameters and static routes.",
    version="1.0.0"
)

# 1. Home API
@app.get("/")
def home():
    return {"message": "Welcome to Super30 FastAPI"}

# 2. Student API
@app.get("/student")
def get_student():
    return {
        "name": "Pavan",
        "batch": "Super30-July-2026",
        "role": "Student"
    }

# 3. Course API
@app.get("/course")
def get_course():
    return {
        "course_name": "Backend Development with FastAPI",
        "mentor": "Sudhanshu",
        "duration": "8 Weeks",
        "topics": [
            "Python",
            "FastAPI",
            "REST API",
            "Database",
            "Deployment"
        ]
    }

# 4. Skills API
@app.get("/skills")
def get_skills():
    return {
        "skills": [
            "Python",
            "FastAPI",
            "SQL",
            "Docker",
            "AWS"
        ]
    }

# 5. Addition API
@app.get("/add/{num1}/{num2}")
def add_numbers(num1: int, num2: int):
    return {"result": num1 + num2}

# 6. Multiplication API
@app.get("/multiply/{num1}/{num2}")
def multiply_numbers(num1: int, num2: int):
    return {"result": num1 * num2}

# 7. Square API
@app.get("/square/{number}")
def calculate_square(number: int):
    return {
        "number": number,
        "square": number ** 2
    }

# 8. Even/Odd API
@app.get("/check/{number}")
def check_even_odd(number: int):
    result_type = "even" if number % 2 == 0 else "odd"
    return {
        "number": number,
        "type": result_type
    }

# 9. Age API
@app.get("/age/{age}")
def evaluate_age(age: int):
    if age < 0:
        category = "Invalid age"
    elif age < 13:
        category = "You are a child."
    elif age <= 19:
        category = "You are a teenager."
    elif age < 60:
        category = "You are an adult."
    else:
        category = "You are a senior citizen."

    return {
        "age": age,
        "message": category
    }

# 10. Table API
@app.get("/table/{number}")
def multiplication_table(number: int):
    table_list = [f"{number} x {i} = {number * i}" for i in range(1, 11)]
    return {
        "number": number,
        "table": table_list
    }

# 11. Profile API
@app.get("/profile/{name}/{age}")
def get_profile(name: str, age: int):
    return {
        "name": name,
        "age": age
    }

# 12. Number Analysis API
@app.get("/number/{number}")
def analyze_number(number: int):
    return {
        "number": number,
        "square": number ** 2,
        "cube": number ** 3,
        "even": (number % 2 == 0)
    }