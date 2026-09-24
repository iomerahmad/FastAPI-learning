from fastapi import FastAPI
from enum import Enum

class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"

app = FastAPI()

@app.get("/model/{model_name}")
async def get_model(model_name: ModelName) -> dict[str, str]:
    if model_name is ModelName.alexnet:
        return {"model_name": model_name, "Message": "Deep learning FTW"}
    if model_name.value == "lenet":
        return {"model_name": model_name, "Message": "leCNN all the images!"}
    return {"model_name": model_name, "Message": "Have some residuals"}

@app.get("/")
async def root() -> dict[str, str]:
    return {"message": "Hello, Omer"}

@app.get("/trade/{trade_id}")
async def get_trade(trade_id: str) -> dict[str, str]:
    return {"trade_id": trade_id} 

@app.get("/users/me")
async def read_user_me() -> dict[str, str]:
    return {"user_id": "the_current_user"}

@app.get("/users/{user_id}")
async def read_user(user_id: int) -> dict[str, int]:
    return {"user_id": user_id}

@app.get("/items/optional")
async def optional(q: str | None = None) -> dict[str, str | None]:
    return {"q": q}

@app.get("/items/required")
async def required(q: str) -> dict[str, str]:
    return {"q": q}




