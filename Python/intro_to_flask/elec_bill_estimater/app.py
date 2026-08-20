from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')
@app.route('/calculate', methods=['POST'])
def calculate():
    units = int(request.form['units'])
    bill = units*5

    if units <= 100:
        message = "Great you are an energy saver!"
    elif units <= 200:
        message = "You are using a moderate amount of energy."
    else:
        message = "You are using a high amount of energy. Consider reducing your consumption."

    return render_template('result.html', bill=bill, message=message)

if __name__ == '__main__':
    app.run(debug=True)
