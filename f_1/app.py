from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "it is very simple <strong> flask </strong> app"

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
