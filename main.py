from fastapi import FASTAPI

app = FASTAPI()

@app.get("/")
async def root() -> dict[str, str]:
    return {"message": "Hello, Omer"}