from fastapi import FastAPI
from pydantic import BaseModel
from project320 import func_320_soliyev, func_ilyas

app = FastAPI(
    title="MMM",
    version="1.0.0",
    description="Платформа для покупки и продажи",
    docs_url="/docs",
    redoc_url="/redoc",
)

# Pythagor funksiyasi
def c2(x: float, y: float) -> float:
    return (x**2 + y**2) ** 0.5

def func_soliyev(x: float, y: float) -> float:
    return x * y

# ✅ Pydantic modeli
class TwoNumbers(BaseModel):
    x: float
    y: float


# --------- GET endpointlar (query params) ---------
@app.get("/c2")
def get_c2(x: float, y: float):
    return {"result": c2(x, y)}

@app.get("/soliyev")
def get_soliyev(x: float, y: float):
    return {"result": func_soliyev(x, y)}


# --------- POST endpointlar (JSON body) ---------
@app.post("/c2")
def post_c2(data: TwoNumbers):
    return {"result": c2(data.x, data.y)}

@app.post("/soliyev")
def post_soliyev(data: TwoNumbers):
    return {"result": func_soliyev(data.x, data.y)}


# Import paytida emas, faqat bevosita ishga tushirganda ishlasin
if __name__ == "__main__":
    print(func_320_soliyev(3, 5))
    print(func_ilyas(3, 4))
