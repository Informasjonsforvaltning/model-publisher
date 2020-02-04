import os
from flask import Flask, Response
from flask_negotiate import produces

app = Flask(__name__)


basedir = os.path.abspath(os.path.dirname(__file__))
data_file = os.path.join(basedir, 'model/model-catalog.ttl')

@app.route('/')
def hello():
    return 'Hello, World!'

@app.route('/model/person')
@produces('text/turtle')
def modelById():
    text = open(data_file, 'r+')
    content = text.read()
    text.close()
    app.logger.info('Content: %s', content)
    return Response(content, mimetype='text/turtle')

@app.route('/ready', methods=['GET'])
def isReady():
    return "OK"


@app.route('/ping', methods=['GET'])
def isAlive():
    return "OK"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
