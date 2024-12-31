from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'
    
@app.route('/ping')
def ping():
    return 'pong!'

@app.route('/message', methods=['POST'])
def post_message():
    data = request.get_json()
    if not data or 'message' not in data:
        return jsonify({'error': 'message field is required'}), 400
    return jsonify({'received': data['message']}), 201
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
