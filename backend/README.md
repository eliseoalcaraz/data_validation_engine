# Data Validation Engine - Backend

A FastAPI-based backend service for validating CSV data files with comprehensive error reporting.

## Setup

### Prerequisites
- Python 3.12+
- pip

### Installation

1. Navigate to the backend directory:
```bash
cd backend
```

2. Create and activate a virtual environment:
```bash
python3 -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Running the Server

Start the development server with hot-reload:
```bash
uvicorn app.main:app --reload
```

The API will be available at `http://localhost:8000`

### API Documentation
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## Testing

Run validation tests on sample data:
```bash
python3 -m app.api.validate
```

This will validate both clean and dirty test datasets located in `test/data/`.

## Project Structure

```
backend/
├── app/
│   ├── main.py              # FastAPI application setup
│   ├── api/
│   │   ├── validate.py      # Validation endpoints
│   │   └── __init__.py
│   ├── core/
│   │   ├── validator.py     # Core validation logic
│   │   └── __init__.py
│   └── __init__.py
├── test/
│   └── data/
│       ├── test_data_clean.csv    # Valid test data
│       └── test_data_dirty.csv    # Invalid test data
└── .venv/                   # Virtual environment (auto-created)
```

## Validation Rules

The validator checks for:
- **Required columns**: `id`, `email`, `age`
- **Data volume**: File must contain more than 10 data rows
- **Email validation**: Must not be empty or null
- **Age validation**: Must be an integer between 18-100

## API Endpoints

### POST /validate
Upload a CSV file for validation.

**Request:**
- Form data with file upload

**Response:**
```json
{
  "status": "pass|fail",
  "errors": [
    {
      "row_index": 1,
      "id": "value",
      "column": "email",
      "error_message": "Email is missing or empty."
    }
  ]
}
```

## Dependencies

See `requirements.txt` for the complete list of dependencies including:
- FastAPI
- Uvicorn
- Pandas
- Python-multipart
