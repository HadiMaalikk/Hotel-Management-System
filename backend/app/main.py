from fastapi import FastAPI

app = FastAPI(title = "Hotel")

@app.get("/")
def health_check():
    return {"status" : "ok"}
