from flask import Flask
app = Flask(__name__)

@app.get("/")
def index(): return "Hello v2\n"

@app.get("/health")
def health(): return {"status": "ok"}
