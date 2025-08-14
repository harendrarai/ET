# ET Calculator Project

A Python project with Flask backend and simple frontend for performing calculations.

## Project Structure
- `src/api/`: Flask backend code
- `src/frontend/`: Frontend HTML/JS files
- `tests/`: Test files
- `requirements.txt`: Project dependencies

## Features
- Multi-number addition
- Dynamic input fields
- Real-time error handling
- Calculation history
- Responsive design

## Setup
1. Create virtual environment: `python3 -m venv venv`
2. Activate virtual environment: `source venv/bin/activate`
3. Install dependencies: `pip install -r requirements.txt`

## Running the Application
1. Start the backend:
   ```
   python src/api/app.py
   ```
   The backend will run on http://localhost:5002

2. Open the frontend:
   - Open `src/frontend/index.html` in a web browser
   - Or use Python's built-in HTTP server:
     ```
     cd src/frontend
     python -m http.server 8090
     ```
     Then visit http://localhost:8090

## Running Tests
Run tests using: `pytest -v`

For coverage report: `pytest --cov=src tests/`
