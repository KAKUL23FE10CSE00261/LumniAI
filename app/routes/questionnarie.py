from flask import Blueprint, render_template, request, session, redirect, url_for

questionnaire_bp = Blueprint(
    "questionnaire",
    __name__
)


@questionnaire_bp.route("/questionnaire", methods=["GET", "POST"])
def questionnaire():

    if request.method == "GET":
        return render_template("questionnaire.html")

    score = {
        "dry": 0,
        "normal": 0,
        "oily": 0,
        "combination": 0
    }

    answers = [
        request.form.get("q1"),
        request.form.get("q2"),
        request.form.get("q3"),
        request.form.get("q4"),
        request.form.get("q5"),
        request.form.get("q6")
    ]

    for answer in answers:

        if answer in score:
            score[answer] += 1

    skin_type = max(score, key=score.get)

    session["skin_type"] = skin_type

    return redirect(url_for("recommendation.recommendation"))