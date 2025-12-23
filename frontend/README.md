# Data Validation Engine - Frontend

A React-based web application for uploading and validating CSV data files with real-time error reporting.

## Setup

### Prerequisites
- Node.js 18+ and npm
- Running backend service (see [../backend/README.md](../backend/README.md))

### Installation

1. Navigate to the frontend directory:
```bash
cd frontend
```

2. Install dependencies:
```bash
npm install
```

## Running the Application

### Development Mode

Start the development server with hot-reload:
```bash
npm start
```

The application will open at `http://localhost:3000`

### Production Build

Create an optimized production build:
```bash
npm run build
```

This generates a `build/` directory with optimized assets ready for deployment.

## Features

- **CSV File Upload**: Upload CSV files for validation
- **Real-time Validation**: Instant feedback on data quality
- **Detailed Error Reports**: View specific errors by row, column, and ID
- **Clean UI**: Simple, user-friendly interface for data validation

## Validation Rules

The frontend communicates with the backend to validate:
- **Required columns**: `id`, `email`, `age`
- **Data volume**: File must contain more than 10 data rows
- **Email validation**: Must not be empty or null
- **Age validation**: Must be an integer between 18-100

## API Integration

The frontend connects to the backend API by automatically deriving the hostname from the current location. 
- In development: `http://localhost:8000`
- In production: Uses the same hostname as the frontend with port 8000

### Upload Endpoint
- **POST** `/validate`
- **Request**: FormData with CSV file
- **Response**: JSON with validation results

## Project Structure

```
frontend/
├── src/
│   ├── App.tsx           # Main application component
│   ├── App.css           # Application styles
│   ├── App.test.tsx      # Tests
│   ├── index.tsx         # Entry point
│   ├── index.css         # Global styles
│   └── react-app-env.d.ts
├── public/
│   ├── index.html        # Main HTML file
│   ├── manifest.json     # PWA manifest
│   └── robots.txt
├── package.json          # Dependencies
├── tsconfig.json         # TypeScript configuration
└── Dockerfile           # Docker configuration
```

## Available Scripts

- `npm start` - Start development server
- `npm run build` - Create production build
- `npm test` - Run tests
- `npm run eject` - Eject from Create React App (irreversible)

## Docker

Build the Docker image:
```bash
docker build -t csv-frontend .
```

Run in Docker:
```bash
docker run -p 3000:3000 csv-frontend
```

Or use docker-compose from the project root:
```bash
sudo docker-compose up frontend
```

## Troubleshooting

### NetworkError when attempting to fetch resource

If you see network errors:
1. Ensure the backend is running on port 8000
2. Check that you're accessing the frontend at `http://localhost:3000`
3. Open browser DevTools Console to see the actual API URL being used
4. The frontend automatically derives the API URL from your current hostname

### Port already in use

If port 3000 is already in use:
```bash
PORT=3001 npm start
```

## Technologies

- React 18
- TypeScript
- Create React App
- Fetch API for HTTP requests
