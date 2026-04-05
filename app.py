from flask import Flask, render_template, request
from password_logic import Password

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def home():
    password = ""
    checker = ""

    if request.method == "POST":
        action = request.form.get("action")

        if action == "generate":
            word1 = request.form["word1"]
            word2 = request.form["word2"]
            word3 = request.form["word3"] or None
            word4 = request.form["word4"] or None
            word5 = request.form["word5"] or None
            # replace = request.form["replace"] or None
            separator = request.form["sep"] or "_"

            P = Password(word1, word2, word3, word4, word5, separator)
            combined = P.combine_words()
            randomized = P.randomize_password(combined)
            checker = P.password_strength_tester(randomized)
            # default face value is unhappy (Not Very Secure)
            # face = "/{/{ url_for('static', filename='images/faces-03.png') /}/}"
            # if checker == "Very Secure":
            #     face = "/{/{ url_for('static', filename='images/faces-01.png') /}/}"
            # elif checker == "Moderately Secure":
            #     face = "/{/{ url_for('static', filename='images/faces-02.png') /}/}"
            password = randomized

        elif action == "check":
            password = request.form["pass"]
            P = Password("", "")
            checker = P.password_strength_tester(password)

    return render_template("index.html", password=password, checker=checker)

if __name__ == "__main__":
    app.run(debug=True)
