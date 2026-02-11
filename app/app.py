from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "SecureCloudOps app is running"

@app.route("/health")
def health():
    return "OK"

app.run(host="0.0.0.0", port=8000)
