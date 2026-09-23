from fastapi import FastAPI

app = FastAPI()

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




