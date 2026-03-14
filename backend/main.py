from fastapi import FastAPI

app = FastAPI()

# Endpointは"/api/hello"("/api"はNginxで設定している。ref: /nginx.conf)
@app.get("/hello")
def read_root():
    return {"Hello": "World"}
