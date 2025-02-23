from flask import Flask, render_template
from flask import Flask, render_template, jsonify  # Added jsonify


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/api/info')
def api_info():
    return jsonify({"message": "Welcome to my Flask web app!"}), 200  # Updated message


if __name__ == '__main__':
    app.run(debug=True)
