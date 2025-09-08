from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Basic route
@app.route('/')
def home():
    return '<h1>Hello, World! This is a Flask web app!</h1><p><a href="/about">About</a> | <a href="/contact">Contact</a></p>'

# Additional routes
@app.route('/about')
def about():
    return '''
    <h1>About Us</h1>
    <p>This is a simple Flask web application.</p>
    <a href="/">Home</a>
    '''

@app.route('/contact')
def contact():
    return '''
    <h1>Contact</h1>
    <p>Email: contact@example.com</p>
    <a href="/">Home</a>
    '''

# Dynamic route with variables
@app.route('/user/<name>')
def user_profile(name):
    return f'<h1>Hello, {name}!</h1><a href="/">Home</a>'

# Route with multiple methods
@app.route('/form', methods=['GET', 'POST'])
def form_example():
    if request.method == 'POST':
        name = request.form.get('name')
        return f'<h1>Hello, {name}! Form submitted successfully!</h1><a href="/form">Back</a>'
    
    return '''
    <form method="POST">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name" required>
        <button type="submit">Submit</button>
    </form>
    <a href="/">Home</a>
    '''

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
