from flask import Flask, request

app = Flask(__name__)

@app.get("/currency")
def get_currency():
    return "USD - 41.5"

if __name__ == '__main__':
    app.run(port=8000)
