from flask import Flask, render_template, request

app = Flask(__name__, template_folder='templates')

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Retrieving data from form fields
        username = request.form.get('username')
        password = request.form.get('password')
        # Simple check for demonstration purposes
        if username and password:
            return f"Hello, {username}! You have submitted the form."
        else:
            return "Please provide both a username and password."
    # If GET request, simply render the form
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
