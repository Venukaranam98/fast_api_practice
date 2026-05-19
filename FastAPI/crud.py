from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()


todos = {}


class Todo(BaseModel):

    title: str

    completed: bool


# CREATE TODO
@app.post("/todos/{todo_id}")

def create_todo(

    todo_id: int,

    todo: Todo

):

    if todo_id in todos:

        raise HTTPException(

            status_code=400,

            detail="Todo ID already exists"

        )

    todos[todo_id] = todo

    return {

        "message": "Todo Created",

        "todo": todo

    }


# GET ALL TODOS
@app.get("/todos")

def get_all_todos():

    return todos


# READ SINGLE TODO
@app.get("/todos/{todo_id}")

def get_todo(todo_id: int):

    if todo_id not in todos:

        raise HTTPException(

            status_code=404,

            detail="Todo not found"

        )

    return todos[todo_id]


# UPDATE TODO
@app.put("/todos/{todo_id}")

def update_todo(

    todo_id: int,

    todo: Todo

):

    if todo_id not in todos:

        raise HTTPException(

            status_code=404,

            detail="Todo not found"

        )

    todos[todo_id] = todo

    return {

        "message": "Todo Updated",

        "todo": todo

    }


# DELETE TODO 
@app.delete("/todos/{todo_id}")

def delete_todo(todo_id: int):

    if todo_id not in todos:

        raise HTTPException(

            status_code=404,

            detail="Todo not found"

        )

    deleted_todo = todos.pop(todo_id)

    return {

        "message": "Deleted Successfully",

        "deleted_todo": deleted_todo

    }