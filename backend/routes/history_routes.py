from flask import Blueprint
from flask import jsonify

history_bp = Blueprint(
    "history_bp",
    __name__
)

# Demo data
history_data = [

    {
        "date": "2026-01",
        "glucose": 140
    },

    {
        "date": "2026-02",
        "glucose": 155
    },

    {
        "date": "2026-03",
        "glucose": 170
    }
]


@history_bp.route(
    "/history",
    methods=["GET"]
)
def history():

    return jsonify(
        history_data
    )