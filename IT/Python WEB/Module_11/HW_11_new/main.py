# main.py
import uvicorn
from fastapi import FastAPI
from src.routes import contacts

app = FastAPI()

app.include_router(contacts.router)

@app.get("/")
async def start():
    return "Welcome to ContactsAPP!"

if __name__ == '__main__':
    uvicorn.run(
        "main:app", reload=True
    )

# uvicorn main:app --reload
