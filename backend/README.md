
# Backend (FastAPI)

## Quickstart

```bash
cd backend
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8000
```

The API will be available at http://localhost:8000 and docs at http://localhost:8000/docs
