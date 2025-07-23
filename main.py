from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['POST'])
def handle_message():
    data = request.get_json()
    print(f"Message received: {data}")
    return 'OK', 200

@app.route('/', methods=['GET'])
def index():
    return 'SuperZaddyBot is alive.', 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
