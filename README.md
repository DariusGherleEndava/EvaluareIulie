# MathServiceProject

## Description

This project is a FastAPI microservice exposing an API for basic mathematical operations: power (pow), n-th Fibonacci number, and factorial. Every request is logged in a SQLite database. The project follows MVCS (Model-View-Controller-Service) best practices and is designed for extensibility and maintainability.

## Technologies Used

- Python 3
- FastAPI
- SQLAlchemy (SQLite)
- Pydantic
- Uvicorn (for running the server)
- Flake8 (linting)

## Project Structure

- `app/models/` - SQLAlchemy models (database)
- `app/schemas/` - Pydantic models (serialization/deserialization)
- `app/services/` - business logic
- `app/api/` - API routes
- `app/db/` - database setup
- `app/main.py` - entry point

## How to Run the Project

### Local (with virtual environment)

1. Create and activate a virtual environment:
   ```powershell
   python -m venv .venv
   .venv\Scripts\activate
   ```
2. Install dependencies:
   ```powershell
   pip install -r requirements.txt
   ```
3. Start the server:
   ```powershell
   uvicorn app.main:app --reload
   ```
4. Access the interactive documentation at [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

### With Docker

1. Build the Docker image:
   ```powershell
   docker build -t mathservice .
   ```
2. Run the container:
   ```powershell
   docker run -p 8000:8000 mathservice
   ```
3. Access the API docs at [http://localhost:8000/docs](http://localhost:8000/docs)

## API Endpoints

- `/pow` POST: `{ "base": 2, "exponent": 8 }`
- `/fibonacci` POST: `{ "n": 10 }`
- `/factorial` POST: `{ "n": 5 }`
- `/logs` GET: returns all request logs

## Other Details

- All requests are logged in the `mathservice.db` SQLite database.
- The code is structured for extensibility and easy maintenance.
- For linting: `flake8 app/`
- For testing: `pytest`

---
