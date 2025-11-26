from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from project320 import func_320_soliyev, func_ilyas
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

app = FastAPI(
    title="Soliyev",
    version="1.0.0",
    description="Платформа для покупки и продажи",
    docs_url="/docs",
    redoc_url="/redoc",
)

def c2(x: float, y: float) -> float:
    return (x**2 + y**2) ** 0.5

def func_soliyev(x: float, y: float) -> float:
    return x * y

class TwoNumbers(BaseModel):
    x: float
    y: float

@app.get("/", response_class=HTMLResponse)
def read_index():
    return (BASE_DIR / "index.html").read_text(encoding="utf-8")

@app.get("/c2")
def get_c2(x: float, y: float):
    return {"result": c2(x, y)}

@app.get("/soliyev")
def get_soliyev(x: float, y: float):
    return {"result": func_soliyev(x, y)}

@app.post("/c2")
def post_c2(data: TwoNumbers):
    return {"result": c2(data.x, data.y)}

@app.post("/soliyev")
def post_soliyev(data: TwoNumbers):
    return {"result": func_soliyev(data.x, data.y)}

if __name__ == "__main__":
    print(func_320_soliyev(3, 5))
    print(func_ilyas(3, 4))