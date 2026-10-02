from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def home():
    print("\n========== NEW VISIT ==========")
    print("IP address :", request.remote_addr)
    print("HTTP method :", request.method)
    print("User-Agent :", request.headers.get("User-Agent"))
    print("Accept-Language :", request.headers.get("Accept-Language"))
    print("Accept :", request.headers.get("Accept"))
    print("Accept-Encoding :", request.headers.get("Accept-Encoding"))
    print("Referer :", request.headers.get("Referer"))
    print("Sec-GPC :", request.headers.get("Sec-GPC"))
    print("================================\n")
    return render_template("index.html")


@app.route("/collect", methods=["POST"])
def collect():
    print("Received :", request.get_json())
    return ""


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=9000, debug=True)
