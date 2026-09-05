# Super30 FastAPI GET API Task

## Objective
The objective of this task is to build foundational backend skills using FastAPI, demonstrating:
- Setting up static and dynamic GET endpoints
- URL path parameter parsing and automatic type validation
- Returning pure JSON responses using Python dictionaries
- Testing and exploring automated Swagger (`/docs`) and ReDoc (`/redoc`) documentation

## Installation
1. Clone this repository:
   ```bash
   git clone <YOUR_GITHUB_REPO_URL>
   cd super30-fastapi-get-api-task

Create and activate a virtual environment:
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

Install dependencies:
pip install -r requirements.txt

Running the Application
Start the Uvicorn ASGI server with live reloading enabled:
uvicorn main:app --reload

The server will start at: http://127.0.0.1:8000

Interactive API Documentation:

Swagger UI: http://127.0.0.1:8000/docs

ReDoc: http://127.0.0.1:8000/redoc

