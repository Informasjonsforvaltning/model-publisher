import os
from flask import Flask, Response

app = Flask(__name__)


basedir = os.path.abspath(os.path.dirname(__file__))
data_file = os.path.join(basedir, 'model/model-catalog.ttl')

@app.route('/')
def hello():
    return 'Hello, World!'

@app.route('/model/person')
def modelById():
    text = open(data_file, 'r+')
    content = text.read()
    text.close()
    app.logger.info('Content: %s', content)
    return Response(content, mimetype='text/turtle')

@app.route('/isReady', methods=['GET'])
def isReady():
    return "OK"


@app.route('/isAlive', methods=['GET'])
def isAlive():
    return "OK"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
