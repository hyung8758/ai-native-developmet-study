from pathlib import Path

from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel, Field

ROOT = Path(__file__).resolve().parent.parent
app = FastAPI(title="Task Board")
app.mount("/static", StaticFiles(directory=ROOT / "static"), name="static")


class TaskCreate(BaseModel):
    title: str = Field(min_length=1, max_length=120)


tasks: list[dict[str, object]] = []
next_id = 1


@app.get("/", response_class=HTMLResponse)
def home() -> str:
    return (ROOT / "static" / "index.html").read_text(encoding="utf-8")


@app.get("/api/tasks")
def list_tasks() -> list[dict[str, object]]:
    return tasks


@app.post("/api/tasks", status_code=201)
def create_task(payload: TaskCreate) -> dict[str, object]:
    global next_id
    title = payload.title.strip()
    if not title:
        raise HTTPException(status_code=422, detail="Task title cannot be blank")
    task: dict[str, object] = {"id": next_id, "title": title, "completed": False}
    next_id += 1
    tasks.append(task)
    return task
