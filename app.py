from flask import Flask, render_template, request, redirect, url_for, jsonify

# Create a simple Flask application
app = Flask(__name__)  # __name__ is the entry point of the program

# Flask App Routing
@app.route("/", methods=["GET"])
def welcome():
    return "<h1>Hello bois</h1>"

@app.route("/index", methods=["GET"])
def index():
    return "<h2>Welcome to the index page</h2>"

# String
# @app.route("/success/<score>")
# def success(score):
#     return "The person has passed and the score is: " + score

# Int
@app.route("/success/<int:score>")
def success(score):
    return "The person has passed and the score is: " + str(score)

@app.route("/fail/<int:score>")
def fail(score):
    return "The person has failed and the score is: " + str(score)

@app.route("/form", methods = ["GET", "POST"])
def form():
    if request.method == "GET":
        return render_template("form.html")
    else:
        maths = float(request.form["maths"])
        science = float(request.form["science"])
        history = float(request.form["history"])
        average_marks = (maths + science + history)/3
        
        res = ""
        if average_marks >= 50:
            res = "success"
        else:
            res = "fail"

        return redirect(url_for(res, score = average_marks))
        # If res = "success" and average_marks = 75.0, url_for generates /success?score=75.0.
        # If res = "fail" and average_marks = 45.0, url_for generates /fail?score=45.0.
        # redirect
        # redirect sends an HTTP redirect response to the browser, instructing it to navigate to the generated URL.
        # The user is effectively redirected to /success or /fail, with the score passed as a query parameter.
        #return render_template("form.html", score = average_marks)

@app.route("/api", methods = ["POST"])
def calculate_sum():
    # get input data that is in json format, convert it to float add them and return in json format
    data = request.get_json()
    a_val = float(dict(data)["a"])
    b_val = float(dict(data)["b"])
    return jsonify(a_val + b_val)

if __name__ == "__main__":
    app.run(debug=True)
