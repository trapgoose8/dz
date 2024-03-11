from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def index():
    return render_template("index.html")


@app.route("/login", methods=['POST'])
def login():
    print(request.form.get('fio'), request.form.get('classes'))
    return render_template("index2.html")


@app.route("/test", methods=['POST'])
def test():
    if request.form['answer'] == "16" and request.form['answer2'] == "256":
        return render_template("index3.html")
    else:
        return render_template("index4.html")


@app.route("/nice")
def nice():
    return render_template("index3.html")


@app.route("/notnice")
def notnice():
    return render_template("index4.html")


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=80)