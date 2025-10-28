# This code imports the Flask library and some functions from it.
from flask import Flask

# Create a Flask application instance
app = Flask(__name__)

# Routes
#===================
# These define which template is loaded, or action is taken, depending on the URL requested
#===================
# Home Page
@app.route('/')
def index():
    # This defines a variable 'studentName' that will be passed to the output HTML
    studentName = "Abdulhameed Tayo Oseni"
    # Render HTML with the name in a H1 tag
    return f"<h1>Hello, {studentName}!</h1>"

# About Page
@app.route('/about/<name>')
def about(name):
    # Render HTML with the name in a H1 tag
    #name="Abdulhameed R Oseni"
    return f"<h1>About {name}!</h1><p>It is easy to create new routes</p>"



# Run application
#=========================================================
# This code executes when the script is run directly.
if __name__ == '__main__':
    print("Starting Flask application...")
    print("Open Your Application in Your Browser: http://localhost:81")
    # The app will run on port 81, accessible from any local IP address
    app.run(host='0.0.0.0', port=81)
