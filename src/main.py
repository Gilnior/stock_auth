from fastapi import FastAPI


app = FastAPI()


@app.get("/health/")
@app.get("/")
def health():
    return {"message": "success"}
