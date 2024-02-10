from flask import Flask
from src.main.routers.tag_routes import tags_routers_bp

app = Flask(__name__)

app.register_blueprint(tags_routers_bp)
