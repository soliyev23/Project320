from project320 import func_320_soliyev, func_ilyas

print(func_320_soliyev(3,5))
print(func_ilyas(3,4))

from funcartur import artur
print(artur(6,3))

@app.get("/c2")
def get_c2(x: float, y: float):
    return {"result": c2(x, y)}
@app.post("/c2")
def post_c2(data: TwoNumbers):
    return {"result": c2(data.x, data.y)}