from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

todos = [
    {
        "id": "1",
        "item" : "Read Stephen King's Duma Key"
    },
    {
        "id": "2",
        "item" : "Go for shopping"
    },
    {
        "id": "3",
        "item" : "Work out"
    },
    {
        "id": "4",
        "item" : "Cook dinner"
    },
]

app = FastAPI()

# Define the CORS origins
origins = [
    "http://localhost:3000",
    "localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"]
)

# Get Route
@app.get("/", tags = ["root"])
async def read_root() -> dict:
    return { "message": "Welcome to FastAPI!" }

# Get Todos Route
@app.get("/todo", tags = ["todos"])
async def get_todos() -> dict:
    return { "data": todos }