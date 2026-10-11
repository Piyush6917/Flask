from flask import Flask

app=Flask(__name__)
@app.route("/")
def home():
    return "Hello!"

# Static Routes

@app.route("/about")
def about():
    return "About Us"

@app.route("/contact")
def contact():
    return "welcome to contact page"

@app.route("/users")
def users():
    return "Welcome to users page"

#dynamic routes

@app.route("/user/<name>")
def user(name):
    return f"hello {name}"


@app.route("/student/<name>/<course>")
def student(name,course):
    return f"{name} is learning {course}"


if __name__=="__main__":
    app.run(debug=True)
    