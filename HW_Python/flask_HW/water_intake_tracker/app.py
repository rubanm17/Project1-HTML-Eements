from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    result = None

    if request.method == "POST":
        name = request.form.get("name", "").strip()
        goal = float(request.form.get("goal", 0))
        consumed = float(request.form.get("consumed", 0))

        if goal > 0:
            progress = min((consumed / goal) * 100, 100)
            remaining = max(goal - consumed, 0)

            result = {
                "name": name,
                "goal": goal,
                "consumed": consumed,
                "progress": round(progress, 1),
                "remaining": remaining
            }

    return render_template("index.html", result=result)


if __name__ == "__main__":
    app.run(debug=True)
