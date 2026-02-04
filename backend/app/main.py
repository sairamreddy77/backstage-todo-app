
from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from typing import List

from . import models, schemas, database, crud

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI(title="Todo API", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def hello():
    return { "message" : "hello"}


@app.get("/api/health")
def health():
    return {"status": "ok"}

@app.get("/api/todos", response_model=List[schemas.TodoOut])
def list_todos(db: Session = Depends(get_db)):
    return crud.get_todos(db)

@app.post("/api/todos", response_model=schemas.TodoOut, status_code=201)
def create_todo(payload: schemas.TodoCreate, db: Session = Depends(get_db)):
    return crud.create_todo(db, payload)

@app.get("/api/todos/{todo_id}", response_model=schemas.TodoOut)
def get_todo(todo_id: int, db: Session = Depends(get_db)):
    todo = crud.get_todo(db, todo_id)
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    return todo

@app.put("/api/todos/{todo_id}", response_model=schemas.TodoOut)
def update_todo(todo_id: int, payload: schemas.TodoUpdate, db: Session = Depends(get_db)):
    todo = crud.update_todo(db, todo_id, payload)
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    return todo

@app.delete("/api/todos/{todo_id}", status_code=204)
def delete_todo(todo_id: int, db: Session = Depends(get_db)):
    ok = crud.delete_todo(db, todo_id)
    if not ok:
        raise HTTPException(status_code=404, detail="Todo not found")
    return None
