from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def home():
    uid = request.args.get('uid')
    page = request.args.get('page')
    print(f"[ANALYTICS] uid={uid} page={page} referer={request.referrer} cookies={dict(request.cookies)}")
    return ''


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=9100, debug=True)
