from flask import Blueprint, request, jsonify

tags_routers_bp = Blueprint('tags_routes', __name__)


@tags_routers_bp.route('/create_tag', methods=['POST'])
def create_tag():
    print(request.json)
    return jsonify({'res': 'ok'})
