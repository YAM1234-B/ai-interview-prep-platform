from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/interview")
def interview():
    role = request.args.get("role")
    difficulty = request.args.get("difficulty")
    return render_template("interview.html", role=role, difficulty=difficulty)

if __name__ == "__main__":
    app.run(debug=True)