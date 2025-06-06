import os
from flask import Flask, jsonify

try:
    from config import GOOGLE_SHEET_KEY, GOOGLE_SERVICE_ACCOUNT_FILE
except Exception:
    GOOGLE_SHEET_KEY = None
    GOOGLE_SERVICE_ACCOUNT_FILE = None

from .google_sheets import get_transactions


def create_app():
    app = Flask(__name__)

    @app.route('/')
    def index():
        return 'Investment Portfolio Tracker'

    @app.route('/transactions')
    def transactions():
        sheet_key = os.environ.get('GOOGLE_SHEET_KEY', GOOGLE_SHEET_KEY)
        creds_file = os.environ.get('GOOGLE_SERVICE_ACCOUNT_FILE', GOOGLE_SERVICE_ACCOUNT_FILE)
        if not sheet_key or not creds_file:
            return 'Google Sheets integration not configured.', 500
        try:
            data = get_transactions(sheet_key, creds_file)
            return jsonify(data)
        except Exception as exc:
            return str(exc), 500

    return app
