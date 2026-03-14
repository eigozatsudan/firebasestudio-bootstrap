from fastapi import FastAPI

app = FastAPI()

# Endpointは"/api/hello"(/apiはNginxで設定している)
@app.get("/hello")
def read_root():
    return {"Hello": "World"}
