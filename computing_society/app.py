from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1> Welcome to My Website </h1>
    <p> This is  built using Flask</p>
    """
@app.route("/about")
def about():
    return "This is the about page"

@app.route("/contact")
def contact():
    return "Contact us here"

if __name__ == "__main__":
    app.run(debug=True)