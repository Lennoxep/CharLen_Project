## CharLen Project

Full‑stack project with:
- **Frontend**: React + Vite + Tailwind CSS in `frontend/`
- **Backend**: FastAPI in `backend/`

The goal is to have a React UI talking to a FastAPI JSON API running locally.

---

## Tech Stack

- **Frontend**
  - React 19
  - Vite
  - Tailwind CSS
  - ESLint

- **Backend**
  - Python 3.14
  - FastAPI
  - Uvicorn
  - python-dotenv

---

## Project Structure

- `frontend/` — React + Vite app (with Tailwind)
- `backend/` — FastAPI app
  - `main.py` — entrypoint with the FastAPI app and basic routes
  - `requirements.txt` — Python dependencies

Root‑level `.gitignore` and `.env` are shared across the project.

---

## Prerequisites

- **Node.js** (LTS recommended)
- **npm** (comes with Node)
- **Python 3.14** (or compatible 3.x)

---

## Setup and Run: Frontend (React + Vite)

From the project root:

```bash
cd frontend
npm install
npm run dev
```

By default Vite serves the app at:

- `http://localhost:5173`

---

## Setup and Run: Backend (FastAPI)

From the project root:

```bash
cd backend
python -m venv venv          # if you don’t already have a venv
source venv/bin/activate     # on macOS / Linux
# .\venv\Scripts\activate    # on Windows PowerShell

pip install -r requirements.txt
uvicorn main:app --reload --port 8000
```

The API will be available at:

- `http://127.0.0.1:8000/` — root endpoint
- `http://127.0.0.1:8000/health` — simple health check

FastAPI’s interactive docs will be at:

- `http://127.0.0.1:8000/docs`

---

## Frontend ↔ Backend Communication

The backend CORS settings in `backend/main.py` currently allow:

- `http://localhost:5173`
- `http://localhost:3000`

So as long as the frontend runs on one of those origins and the backend on port `8000`, the browser should allow requests from the React app to the FastAPI API.

---

## Environment Variables

- Root `.gitignore` is configured to ignore:
  - `.env`
  - `.env.*`

Recommended usage:

- **Backend**: load configuration (e.g. database URL, secret keys) from a root `.env` file using `python-dotenv`.
- **Frontend**: if needed, use `frontend/.env` with `VITE_`‑prefixed variables (e.g. `VITE_API_URL=http://127.0.0.1:8000`); remember these are **not secrets**.

---

## Next Steps / TODO (high‑level)

- Add real API routes under `backend/api/`
- Define data models in `backend/models/` and `backend/schemas/`
- Build React pages/components in `frontend/src/` that call the FastAPI routes
