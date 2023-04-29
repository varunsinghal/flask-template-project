from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
app.url_map.strict_slashes = False

CORS(app)
app.config["CORS_HEADERS"] = "Content-Type"
