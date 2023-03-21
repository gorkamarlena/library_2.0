# app/__init__.py

from flask import Flask    # 1

app = Flask(__name__)      # 2

from app import routes     # 3