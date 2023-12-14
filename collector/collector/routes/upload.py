import os

from flask import request, current_app, jsonify, Blueprint
from collector.auth import authclass


upload_bp = Blueprint(name="upload_endpoint", import_name=__name__)


@upload_bp.route("/upload-page", methods=["POST"])
@authclass.login_required
def upload_page():
    if file := request.files.get("file"):
        filepath = os.path.join(
            current_app.config.get("UPLOAD_FOLDER", "/tmp"), file.filename
        )
        file.save(filepath)
        
    return jsonify({"status": "ok"})
