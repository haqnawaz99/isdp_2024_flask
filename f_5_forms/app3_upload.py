from flask import Flask, render_template, request
import pandas as pd  # For handling Excel files

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


@app.route('/file_upload', methods=['GET', 'POST'])
def file_upload():
    if request.method == 'POST':
        # Retrieving the file from the form submission
        file = request.files.get('file')
        
        # Checking if file exists
        if not file:
            return "No file uploaded."

        # Handling text files
        if file.content_type == 'text/plain':
            return file.read().decode('utf-8')  # Decode and return the content of the text file

        # Handling Excel files (.xlsx or .xls)
        elif (file.content_type == 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet' or 
              file.content_type == 'application/vnd.ms-excel'):
            # Read Excel file into a DataFrame
            df = pd.read_excel(file)
            # Return DataFrame as an HTML table
            return df.to_html()

        else:
            return "Unsupported file type."

    # Render the file upload form on GET request
    return render_template('file_upload.html')

if __name__ == '__main__':
    app.run(debug=True)
