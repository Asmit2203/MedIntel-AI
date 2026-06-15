from flask import Flask
from flask_cors import CORS

import os

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

# -------------------------
# Register Routes
# -------------------------

app.register_blueprint(
    upload_bp
)

app.register_blueprint(
    chat_bp
)

app.register_blueprint(
    history_bp
)

# -------------------------
# Health Check
# -------------------------

@app.route("/")
def home():

    return {
        "success": True,
        "message": "🏥 MedIntel API is running!",
        "version": "1.0.0"
    }

# -------------------------
# Render / Local Startup
# -------------------------

if __name__ == "__main__":

    port = int(
        os.environ.get(
            "PORT",
            5000
        )
    )

    app.run(
        host="0.0.0.0",
        port=port,
        debug=False
    )