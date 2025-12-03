from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
import functions as p
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent

app = FastAPI(
    title="Soliyev",
    version="1.0.0",
    description="Платформа для покупки и продажи",
    docs_url="/docs",
    redoc_url="/redoc",
)

class TwoNumbers(BaseModel):
    x: float
    y: float

@app.get("/", response_class=HTMLResponse)
def read_index():
    return (BASE_DIR / "index.html").read_text(encoding="utf-8")

@app.get("/ilyas")
def get_ilyas(x: float, y: float):
    return {"result": p.func_ilyas(x, y)}

@app.get("/soliyev")
def get_soliyev(x: float, y: float):
    return {"result": p.func_320_soliyev(x, y)}

@app.get("Artur")
def get_artur(x: float, y: float):
    return {"result": p.artur(x,y)}

@app.get("/inoyatov")
def get_inoyatov(x: float, y: float ):
    return {"result":p.inoyatov(x, y)}

@app.post("/ilyas")
def post_ilyas(data: TwoNumbers):
    return {"result": p.func_ilyas(data.x, data.y)}

@app.post("/soliyev")
def post_soliyev(data: TwoNumbers):
    return {"result": p.func_320_soliyev(data.x, data.y)}

@app.post("/artur")
def post_artur(data: TwoNumbers):
    return {"result": p.artur(data.x, data.y)}
    
@app.post("/inoyatov")
def post_inoyatov(data: TwoNumbers):
    return {"result": p.inoyatov(data.x, data.y)}


@app.get("/Shakirjanov")
def get_p1(x: float, y: float):
    return {"result": p.p1(x, y)}

@app.post("/Shakirjanov")
def post_p1(data: TwoNumbers):
    return {"result": p.p1(data.x,data.y)}

if __name__ == "__main__":
    print(p.func_320_soliyev(3, 5))
    print(p.func_ilyas(3, 4))
    print(p.func_320_soliyev(3, 5))
    print(p.func_ilyas(3, 4))
    print(p.inoyatov(25, 5))
    print(p.p1(2,3))


