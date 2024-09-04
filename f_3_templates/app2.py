from flask import Flask, render_template

app = Flask(__name__, template_folder='templates')

@app.route('/')
def index():
    myvalue = 'loop'
    myresult = 10 + 20
    xyz = 'Python'
    return render_template('index2.html', myvalue=myvalue, myresult=myresult, course= xyz)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
