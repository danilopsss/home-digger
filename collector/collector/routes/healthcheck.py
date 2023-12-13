from flask import jsonify, Blueprint
from collector.auth import authclass


healthcheck_bp = Blueprint(name="healthcheck", import_name=__name__)

@healthcheck_bp.route("/ping", methods=["GET"])
@authclass.login_required
def healthcheck():
    return jsonify({"response": "pong"})
