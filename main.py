import uvicorn
from fastapi import FastAPI


app = FastAPI()


@app.get("/")
def index():
    return {'result': True}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
