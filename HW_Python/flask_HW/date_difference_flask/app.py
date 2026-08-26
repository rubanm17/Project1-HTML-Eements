from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    error = None

    if request.method == "POST":
        date1 = request.form.get("date1", "")
        date2 = request.form.get("date2", "")

        try:
            first_date = datetime.strptime(date1, "%Y-%m-%d")
            second_date = datetime.strptime(date2, "%Y-%m-%d")

            difference = abs((second_date - first_date).days)

            result = {
                "date1": first_date.strftime("%d %B %Y"),
                "date2": second_date.strftime("%d %B %Y"),
                "days": difference
            }
        except ValueError:
            error = "Please enter two valid dates."

    return render_template("index.html", result=result, error=error)


if __name__ == "__main__":
    app.run(debug=True)
