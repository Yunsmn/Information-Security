from flask import Flask, render_template, make_response, request, send_from_directory
from datetime import datetime
import secrets
import os

app = Flask(__name__)

IMAGES_DIR = os.path.join(os.path.dirname(__file__), 'images')

hits = []


@app.route('/')
def home():
    aid = request.cookies.get('aid')
    is_new = aid is None

    if is_new:
        aid = secrets.token_hex(8)

    response = make_response(render_template('index.html'))

    if is_new:
        response.set_cookie(key='aid', value=aid)

    response.headers["X-Lab-Message"] = "Hello from the Flask server"
    print("\n--- HTTP REQUEST HEADERS ---")
    print(request.headers)
    print("--- HTTP RESPONSE HEADERS ---")
    print(response.headers)

    return response


@app.route('/images/<path:filename>')
def tracker(filename):
    aid = request.cookies.get('aid') or secrets.token_hex(8)
    print(f"[TRACKER] aid={aid} file={filename} referer={request.referrer}")

    response = send_from_directory(IMAGES_DIR, filename)
    response.set_cookie('aid', aid)
    return response


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8002, debug=True)
