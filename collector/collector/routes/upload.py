import os

from uuid import uuid4
from flask import request, current_app, jsonify, Blueprint
from collector.auth import authclass


upload_bp = Blueprint(name="upload_endpoint", import_name=__name__)


@upload_bp.route("/upload-page", methods=["POST"])
@authclass.login_required
def upload_page(): 
    if file := request.form.get("file"):
        filename = str(uuid4())
        saving_path = current_app.config.get("UPLOAD_FOLDER", "")
        with open(os.path.join(saving_path, filename), "w") as f:
            f.write(file)
    return jsonify({"status": "ok"})
