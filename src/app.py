from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": "Hello, this is my Flask web app!"})  # ✅ Ensure JSON response

if __name__ == '__main__':
    app.run(debug=True)
