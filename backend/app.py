from flask import Flask

from flask_cors import CORS

from routes.upload_routes import (
    upload_bp
)

from routes.chart_routes import (
    chat_bp
)

from routes.history_routes import (
    history_bp
)

app = Flask(__name__)

CORS(app)

app.register_blueprint(
    upload_bp
)

app.register_blueprint(
    chat_bp
)

app.register_blueprint(
    history_bp
)


@app.route("/")
def home():

    return {
        "message":
        "Medical Report Analyzer API Running"
    }


if __name__ == "__main__":

    app.run(
        debug=True,
        host="0.0.0.0",
        port=5000
    )