from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

tasks = []

class TaskRequest(BaseModel):
    action: str
    task: str = None

@app.post("/tasks")
def manage_tasks(request: TaskRequest):
    if request.action == "add" and request.task:
        tasks.append(request.task)
        return {"message": f"Task '{request.task}' added.", "tasks": tasks}
    elif request.action == "list":
        return {"tasks": tasks}
    elif request.action == "remove" and request.task:
        if request.task in tasks:
            tasks.remove(request.task)
            return {"message": f"Task '{request.task}' removed.", "tasks": tasks}
        else:
            return {"error": "Task not found.", "tasks": tasks}
    return {"error": "Invalid action or missing task."}
