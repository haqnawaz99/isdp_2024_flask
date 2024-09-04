from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>Hello ISDP</h1>"



@app.route('/salam')
def salam():
    return "السلام علیکم "

@app.route('/isdp')
def xyz():
    return '<h1>Welcome to programming class</h1>'

@app.route('/greet/<name>')
def greet(name):
    return f"Asalamualaikum {name}"

@app.route('/square/<int:num>')
def sq(num):
    return f"The square of {num} = {num * num}"



if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
