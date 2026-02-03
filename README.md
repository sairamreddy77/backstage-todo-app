
# Fullstack Todo — React + FastAPI + SQLite

A minimal, clean, and fast Todo application built with React (Vite), FastAPI, and SQLite. Features full CRUD, CORS, and a simple dark UI.

## Stack
- **Frontend**: React + Vite
- **Backend**: FastAPI, SQLAlchemy, Pydantic v2
- **Database**: SQLite

## Running locally

### 1) Backend
```bash
cd backend
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8000
```

Open API docs: http://localhost:8000/docs

### 2) Frontend
In a new terminal:
```bash
cd frontend
npm install
npm run dev
```

App: http://localhost:5173

## Project structure
```
react-fastapi-sqlite-todo/
├── backend/
│   ├── app/
│   │   ├── crud.py
│   │   ├── database.py
│   │   ├── main.py
│   │   ├── models.py
│   │   └── schemas.py
│   ├── requirements.txt
│   └── README.md
├── frontend/
│   ├── index.html
│   ├── package.json
│   ├── vite.config.js
│   ├── src/
│   │   ├── App.jsx
│   │   ├── main.jsx
│   │   └── styles.css
│   └── README.md
└── README.md
```

## Notes
- The frontend dev server proxies `/api` calls to the backend at `http://localhost:8000`.
- SQLite DB file `todo.db` is created in `backend/` automatically on first run.
- For production, build the frontend and serve static files from a proper web server or mount with FastAPI.
