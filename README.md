# Data Validation Engine

A full-stack application for validating CSV data files with a React frontend and FastAPI backend, deployed using Docker and Docker Compose.

## Project Overview

This application allows users to upload CSV files and validate them against specific rules:
- Required columns: `id`, `email`, `age`
- Data volume: Must contain more than 10 rows
- Email validation: Non-empty email addresses
- Age validation: Integer between 18-100

## Architecture

```
data-validation-engine/
├── backend/                 # FastAPI REST API
│   ├── app/
│   │   ├── main.py         # FastAPI application
│   │   ├── api/            # API endpoints
│   │   └── core/           # Core validation logic
│   ├── requirements.txt
│   ├── Dockerfile
│   └── README.md
├── frontend/               # React TypeScript application
│   ├── src/
│   │   ├── App.tsx         # Main component
│   │   └── ...
│   ├── package.json
│   ├── Dockerfile
│   └── README.md
├── docker-compose.yml      # Multi-container orchestration
└── README.md
```

## Quick Start

### Prerequisites
- Docker and Docker Compose
- Git

### Running with Docker Compose

1. Clone the repository:
```bash
cd /path/to/project
```

2. Start all services:
```bash
sudo docker-compose up --build
```

3. Open your browser:
- Frontend: `http://localhost:3000`
- Backend API: `http://localhost:8000`
- API Docs: `http://localhost:8000/docs`

### Stopping Services

```bash
sudo docker-compose down
```

## Local Development Setup

### Backend Setup

See [backend/README.md](./backend/README.md) for detailed instructions.

```bash
cd backend
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Backend runs on `http://localhost:8000`

### Frontend Setup

See [frontend/README.md](./frontend/README.md) for detailed instructions.

```bash
cd frontend
npm install
npm start
```

Frontend runs on `http://localhost:3000`

## Services

### Backend (FastAPI)
- **Port**: 8000
- **Framework**: FastAPI with Uvicorn
- **Language**: Python 3.12
- **Key Dependencies**: pandas, fastapi, uvicorn

**Endpoints**:
- `POST /validate` - Upload and validate CSV file
- `GET /docs` - Swagger UI documentation
- `GET /redoc` - ReDoc documentation

### Frontend (React)
- **Port**: 3000
- **Framework**: React 18 with TypeScript
- **Build Tool**: Create React App
- **Key Dependencies**: React, TypeScript

**Features**:
- CSV file upload
- Real-time validation
- Detailed error reports in table format
- Success/failure status display

## Docker Compose Configuration

The `docker-compose.yml` orchestrates both services:

```yaml
services:
  backend:
    - Builds from `backend/Dockerfile`
    - Exposes port 8000
    - Mounts code for live reload
    - Runs with uvicorn auto-reload

  frontend:
    - Builds from `frontend/Dockerfile`
    - Exposes port 3000
    - Mounts code for hot reload
    - Passes API URL as build argument
```

## File Upload & Validation Flow

1. User selects CSV file in React frontend
2. File is sent to `/validate` endpoint via POST request
3. Backend receives file and validates:
   - Required columns present
   - Data volume check (>10 rows)
   - Individual row validations
4. Validation results returned as JSON
5. Frontend displays results in table or success message

## Example CSV Format

**Valid Data** (`test/data/test_data_clean.csv`):
```
id,name,email,age,department
101,Clean Record,clean.1@xovate.com,25,Engineering
102,Perfect Data,clean.2@xovate.com,30,Sales
...
```

**Invalid Data** (`test/data/test_data_dirty.csv`):
- Missing emails
- Invalid ages
- Insufficient rows

## Troubleshooting

### Docker Permission Denied

If you see "Permission denied" errors:
```bash
sudo usermod -aG docker $USER
newgrp docker
```

Then run without `sudo`:
```bash
docker-compose up --build
```

### Port Already in Use

If ports 3000 or 8000 are in use:
```bash
# Kill process on port 3000
sudo lsof -i :3000 | grep LISTEN | awk '{print $2}' | xargs kill -9

# Kill process on port 8000
sudo lsof -i :8000 | grep LISTEN | awk '{print $2}' | xargs kill -9
```

### NetworkError in Frontend

Ensure:
1. Backend is running on port 8000
2. Frontend is accessed via `http://localhost:3000`
3. Check browser console for actual API URL being used

### Container Logs

View logs for debugging:
```bash
# All services
sudo docker-compose logs -f

# Specific service
sudo docker-compose logs -f backend
sudo docker-compose logs -f frontend
```

## Development Workflow

### Backend Development
1. Edit code in `backend/app/`
2. Changes auto-reload with uvicorn `--reload`
3. Test via `http://localhost:8000/docs`

### Frontend Development
1. Edit code in `frontend/src/`
2. Changes auto-refresh in browser
3. Check console for errors and API calls

### Building for Production

**Frontend Production Build**:
```bash
cd frontend
npm run build
```

**Backend Production Build**:
- Use the Dockerfile as-is for container deployment

## Technologies Used

### Backend
- **FastAPI** - Modern Python web framework
- **Uvicorn** - ASGI server
- **Pandas** - Data processing and CSV handling
- **Python 3.12** - Latest stable Python

### Frontend
- **React 18** - UI library
- **TypeScript** - Type-safe JavaScript
- **Create React App** - Build tooling
- **Fetch API** - HTTP client

### DevOps
- **Docker** - Containerization
- **Docker Compose** - Multi-container orchestration
- **NGINX** - Reverse proxy (optional for production)

## Repository Information

- **Repository**: data_validation_engine
- **Owner**: eliseoalcaraz
- **Current Branch**: main
- **License**: [Add your license]

## Contributing

1. Create a feature branch
2. Make changes in both frontend/backend as needed
3. Test with `docker-compose up --build`
4. Submit pull request

## Next Steps

- Add authentication and authorization
- Implement database for storing validation results
- Add file history and export features
- Create mobile-friendly responsive design
- Add data visualization for error patterns
- Implement batch processing for large files
- Add webhook notifications for validation results

## Support

For issues or questions:
1. Check the individual README files in `backend/` and `frontend/`
2. Review Docker logs: `sudo docker-compose logs`
3. Check browser DevTools Console for frontend errors
4. Visit API docs at `http://localhost:8000/docs`
