
from sqlalchemy.orm import Session
from datetime import datetime

from . import models, schemas

def get_todos(db: Session):
    return db.query(models.Todo).order_by(models.Todo.created_at.desc()).all()

def get_todo(db: Session, todo_id: int):
    return db.query(models.Todo).filter(models.Todo.id == todo_id).first()

def create_todo(db: Session, payload: schemas.TodoCreate):
    todo = models.Todo(title=payload.title, completed=False)
    db.add(todo)
    db.commit()
    db.refresh(todo)
    return todo

def update_todo(db: Session, todo_id: int, payload: schemas.TodoUpdate):
    todo = get_todo(db, todo_id)
    if not todo:
        return None
    if payload.title is not None:
        todo.title = payload.title
    if payload.completed is not None:
        todo.completed = payload.completed
    todo.updated_at = datetime.utcnow()
    db.commit()
    db.refresh(todo)
    return todo

def delete_todo(db: Session, todo_id: int) -> bool:
    todo = get_todo(db, todo_id)
    if not todo:
        return False
    db.delete(todo)
    db.commit()
    return True
