from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse, PlainTextResponse
from fastapi.templating import Jinja2Templates
import uvicorn

from models import Task, TaskInn


app = FastAPI()
templates = Jinja2Templates(directory="templates")


tasks = [] 


@app.get("/tasks/", response_model=list[Task])
async def read_item(request: Request, id: str):
    if tasks:
        return templates.TemplateResponse("task.html", {"request": request, "tasks": tasks})
    else:
        raise HTTPException(status_code = 404, detail='Task not found')


@app.get("/tasks/{id}", response_model=list[Task])
async def read_item(request: Request, id: str):
    for task in tasks:
        if task['id'] == id:
            return task
    return templates.TemplateResponse("task_1.html", {"request": request, "task": task})


@app.post('/tasks/', response_model= Task)
async def create_task(new_task: TaskInn):
    tasks.append(Task(id = len(tasks)+1), title= new_task.title, description= new_task.description, completed = new_task.completed)
    return tasks


@app.put('/tasks/', response_model= list[Task])
async def edit_task(task_id: int, new_task: TaskInn):
    for i in range(0, len(tasks)):
        if tasks[i].id == task_id:
            curent_task = tasks[task_id - 1]
            curent_task.title = new_task.title
            curent_task.description = new_task.description
            curent_task.completed= new_task.scompleted
            return curent_task
    raise HTTPException(status_code=404, detail= 'Task not found') 


@app.delete('/tasks/', response_model= dict)
async def delete_task(task_id: int):
    curent_task = None
    for i in range(0, len(tasks)):
        if tasks[i].id == task_id:
            tasks.remove(tasks[i])
            return {'message': 'task was delited'}
    raise HTTPException(status_code=404, detail= 'Task not found') 


