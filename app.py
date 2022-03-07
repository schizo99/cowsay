# Required imports
import socket
import os
from flask import Flask, request, jsonify, make_response
import logging
import json
# Initialize Flask app
app = Flask(__name__)

LOGLEVEL = logging.DEBUG if os.getenv("LOGLEVEL", "info").lower() == "debug" else logging.INFO
VERSION = os.getenv("VERSION", "unknown version")
logging.basicConfig(level=LOGLEVEL, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


def print_cow(message):
    
    return f"""  {"_"*len(message)}
| {message} |
  {"="*len(message)}
    \\
     \\
      ^__^
      (oo)\_______
      (__)\       )\/\\
          ||----w |
          ||     ||

from: {socket.gethostname()}
version: {VERSION}
""".format(message)

@app.route('/', methods=['GET'])
def default():

    message = request.args.get("message", "The silent type?")
    response = make_response(print_cow(message), 200)
    response.mimetype = "text/plain"
    return response
    
port = int(os.environ.get('PORT', 8080))
if __name__ == '__main__':
    app.run(threaded=True, host='0.0.0.0', port=port)