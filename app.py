from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    print("Velox Inventory is running! Open http://127.0.0.1:5000 in your browser.")
    app.run(debug=True)