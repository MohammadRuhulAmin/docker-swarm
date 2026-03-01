from fastapi import FastAPI
import socket

app = FastAPI()

@app.get("/")
def read_root():
    return {
        "message": "Hello World from Docker Swarm!",
        "hostname": socket.gethostname()
    }