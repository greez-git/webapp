from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/salvador")
def salvador():
    return "Hello, Salvador"

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)

