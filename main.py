from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "on web-site"}


if __name__ == "__main__":
    uvicorn.run("main:backend", port=8000, host="0.0.0.0", reload=True)
