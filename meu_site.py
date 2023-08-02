from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def homepage():
    return render_template("homepage.html")

@app.route("/contactme")
def contatos():
    return render_template("contatos.html")

@app.route("/users/<username>")
def users(username: str):
    return render_template("users.html", username=username)


if __name__ == '__main__':
   app.run(debug=True)