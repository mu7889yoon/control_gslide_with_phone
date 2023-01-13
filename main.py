import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import pyautogui
import os
import setup

app = FastAPI()

origins = [
    "http://localhost",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
    
@app.get("/next")
async def next():
    pyautogui.press('right')
    return {"message": "Next"}

@app.get("/prev")
async def prev():
    pyautogui.press('left')
    return {"message": "Prev"}


if __name__ == "__main__":
    setup.main()
    import conf
    uvicorn.run(app, host=conf.computer_ip)
