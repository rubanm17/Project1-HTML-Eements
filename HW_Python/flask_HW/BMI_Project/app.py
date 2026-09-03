from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    bmi = None
    category = None

    if request.method == "POST":
        try:
            weight = float(request.form["weight"])
            height = float(request.form["height"])

            if weight > 0 and height > 0:
                bmi = weight / (height ** 2)
                bmi = round(bmi, 2)

                if bmi < 18.5:
                    category = "Underweight"
                elif bmi < 25:
                    category = "Normal weight"
                elif bmi < 30:
                    category = "Overweight"
                else:
                    category = "Obese"
            else:
                category = "Please enter positive values."
        except ValueError:
            category = "Please enter valid numbers."

    return render_template("index.html", bmi=bmi, category=category)

if __name__ == "__main__":
    app.run(debug=True)
