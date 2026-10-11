from flask import Flask

app = Flask(__name__)

# Original home route
@app.route('/')
def home():
    return "Hello, World!"

# New route 1: About Page
@app.route('/about')
def about():
    return "This is a simple Flask web application with multiple routes."

# New route 2: Dynamic Route with a variable
@app.route('/user/<name>')
def user_profile(name):
    return f"Hello, {name}! Welcome to your profile page."

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
