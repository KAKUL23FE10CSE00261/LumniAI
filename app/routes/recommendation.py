from flask import Blueprint, render_template, session, redirect, url_for

from app.services.recommendation_engine import get_recommendation

recommendation_bp = Blueprint(
    "recommendation",
    __name__
)


@recommendation_bp.route("/recommendation")
def recommendation():

    skin_issue = session.get("skin_issue")
    skin_type = session.get("skin_type")

    if skin_issue is None or skin_type is None:
        return redirect(url_for("questionnaire.questionnaire"))

    recommendation = get_recommendation(
        skin_issue,
        skin_type
    )

    return render_template(
        "recommendation.html",
        skin_issue=skin_issue,
        skin_type=skin_type,
        recommendation=recommendation
    )