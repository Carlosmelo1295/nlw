from flask import Blueprint, request, jsonify

from src.errors.error_handle import error_handle
from src.views.http_types.http_request import HttpRequest
from src.views.tag_creator_view import TagCreatorView

tags_routers_bp = Blueprint('tags_routes', __name__)


@tags_routers_bp.route('/create_tag', methods=['POST'])
def create_tag():
    try:
        tag_creator = TagCreatorView()
        http_request = HttpRequest(body=request.json)
        response = tag_creator.validade_and_create(http_request)
    except Exception as exception:
        response = error_handle(exception, 400)

    return jsonify(response.body)
