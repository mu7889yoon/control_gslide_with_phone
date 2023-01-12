import conf
import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import pyautogui

app = FastAPI()

origins = [
    "http://localhost",
    conf.phone_ip
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
    # pyautogui.press('right')
    print("next")
    return {"message": "Next"}

@app.get("/prev")
async def prev():
    # pyautogui.press('left')
    print("prev")
    return {"message": "Prev"}
