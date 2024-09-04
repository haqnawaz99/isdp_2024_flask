from flask import Flask, render_template, request

app = Flask(__name__, template_folder='templates')

# Define constant username and password for login
VALID_USERNAME = 'admin'
VALID_PASSWORD = '123'

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Retrieving data from form fields
        username = request.form.get('username')
        password = request.form.get('password')
        
        # Check if username and password match predefined values
        if username == VALID_USERNAME and password == VALID_PASSWORD:
            return f"Login Successful! Welcome, {username}."
        else:
            return "Login Failed! Invalid username or password."
    
    # If GET request, simply render the form
    return render_template('index.html')

@app.route('/file_upload', methods=['get','POST'])
def file_upload():
    return render_template('file_upload.html')

if __name__ == '__main__':
    app.run(debug=True)
