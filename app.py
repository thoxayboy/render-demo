from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Xin chào! Đây là Flask web cơ bản."

if __name__ == '__main__':
    app.run(debug=True)
