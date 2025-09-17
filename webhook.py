from flask import Flask, request

app = Flask(__name__)

@app.route("/tebex-webhook", methods=["POST"])
def tebex_webhook():
    data = request.get_json()
    print("Webhook received:", data)
    return "", 200 

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
