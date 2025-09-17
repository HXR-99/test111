from flask import Flask, request
print("hello")
app = Flask(__name__)

@app.route("/tebex-webhook", methods=["POST"])
def tebex_webhook():
    data = request.get_json()
    print("Webhook received:", data)
    return "", 200 



