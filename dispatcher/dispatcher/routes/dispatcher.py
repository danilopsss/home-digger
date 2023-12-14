from flask import request, Blueprint
from dispatcher.auth import authclass
from dispatcher.core.broker.utils import dispatch_message


dispatcher_bp = Blueprint(name="dispatcher", import_name=__name__)


@dispatcher_bp.route("/deliver", methods=["POST"])
@authclass.login_required
@dispatch_message
def dispatcher():
    return request.json
