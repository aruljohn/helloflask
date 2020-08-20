from flask import Flask
import os
from datetime import datetime


app = Flask(__name__)

@app.route("/")
def index():
    return f'<h1>hello flask</h1> {datetime.now().astimezone().strftime("%Y-%m-%d %H:%M:%S %z")}'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
