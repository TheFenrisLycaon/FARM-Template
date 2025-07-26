# FARM Template

A modern, production-ready full stack template combining Next.js and FastAPI, designed to help you build and scale your applications quickly.

## Features

- **Full Stack Template**: Includes a Next.js frontend and a FastAPI backend for rapid development.
- **Authentication**: Integrated with Clerk for seamless user authentication and management.
- **API Ready**: Backend is structured for scalable API development with FastAPI.
- **Modern UI**: Styled with Tailwind CSS for a clean, responsive interface.
- **Docker Support**: Easy deployment and local development with Docker.
- **TypeScript & Linting**: Type safety and code quality enforced throughout the project.

## Getting Started

1. **Clone the repository**

   ```sh
   git clone <your-repo-url>
   cd FARM-template
   ```

2. **Frontend Setup**

   ```sh
   cd frontend
   npm install
   npm run dev
   ```

3. **Backend Setup**

   ```sh
   cd backend
   pip install -r requirements.txt  # or use poetry install if using Poetry
   uvicorn app.main:app --reload
   ```

4. **Docker (Optional)**

   ```sh
   docker-compose up --build
   ```

## Folder Structure

- `frontend/` - Next.js app (React, Tailwind CSS, TypeScript)
- `backend/` - FastAPI app (Python)
