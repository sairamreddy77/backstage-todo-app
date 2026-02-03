
import React, { useEffect, useState } from 'react'

const api = {
  async list() {
    const r = await fetch('/api/todos')
    return r.json()
  },
  async create(title) {
    const r = await fetch('/api/todos', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ title })
    })
    return r.json()
  },
  async update(id, data) {
    const r = await fetch(`/api/todos/${id}`, {
      method: 'PUT',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(data)
    })
    return r.json()
  },
  async remove(id) {
    await fetch(`/api/todos/${id}`, { method: 'DELETE' })
  }
}

export default function App() {
  const [todos, setTodos] = useState([])
  const [text, setText] = useState('')
  const [loading, setLoading] = useState(true)

  const refresh = async () => {
    setLoading(true)
    const data = await api.list()
    setTodos(data)
    setLoading(false)
  }

  useEffect(() => { refresh() }, [])

  const add = async (e) => {
    e.preventDefault()
    if (!text.trim()) return
    const created = await api.create(text.trim())
    setTodos([created, ...todos])
    setText('')
  }

  const toggle = async (t) => {
    const updated = await api.update(t.id, { completed: !t.completed })
    setTodos(todos.map(x => x.id === t.id ? updated : x))
  }

  const rename = async (t, title) => {
    const updated = await api.update(t.id, { title })
    setTodos(todos.map(x => x.id === t.id ? updated : x))
  }

  const remove = async (t) => {
    await api.remove(t.id)
    setTodos(todos.filter(x => x.id !== t.id))
  }

  return (
    <div className="container">
      <h1>✅ FastAPI + React + SQLite — Todo</h1>
      <div className="card">
        <form onSubmit={add} className="row">
          <input
            type="text"
            placeholder="Add a new task..."
            value={text}
            onChange={e => setText(e.target.value)}
          />
          <button type="submit">Add</button>
        </form>

        {loading ? (
          <p>Loading...</p>
        ) : (
          <ul>
            {todos.length === 0 && <small className="muted">No tasks yet. Add your first one! 🎯</small>}
            {todos.map(t => (
              <TodoItem key={t.id} todo={t} onToggle={() => toggle(t)} onRename={(title) => rename(t, title)} onDelete={() => remove(t)} />
            ))}
          </ul>
        )}
      </div>
    </div>
  )
}

function TodoItem({ todo, onToggle, onRename, onDelete }) {
  const [editing, setEditing] = useState(false)
  const [val, setVal] = useState(todo.title)

  const submit = async (e) => {
    e.preventDefault()
    if (val.trim() && val !== todo.title) {
      await onRename(val.trim())
    }
    setEditing(false)
  }

  return (
    <li>
      <input type="checkbox" checked={todo.completed} onChange={onToggle} />
      <div className={`title ${todo.completed ? 'completed' : ''}`}>
        {editing ? (
          <form onSubmit={submit}>
            <input value={val} onChange={e => setVal(e.target.value)} onBlur={submit} autoFocus />
          </form>
        ) : (
          <span onDoubleClick={() => setEditing(true)}>{todo.title}</span>
        )}
      </div>
      <div className="actions">
        <button className="secondary" onClick={() => setEditing(v => !v)}>{editing ? 'Save' : 'Edit'}</button>
        <button className="secondary" onClick={onDelete}>Delete</button>
      </div>
    </li>
  )
}
