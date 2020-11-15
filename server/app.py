from flask import Flask, jsonify
from flask_cors import CORS

# config options
debug = True

# instantiate app
app = Flask(__name__)
app.config.from_object(__name__)

# enable cors
CORS(app, resources={r'/*': {'origins': '*'}})

# sanity checking route
@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')

if __name__ == '__main__':
    app.run()