import os
import logging
from flask import Flask, Response
import rdflib

import config

app = Flask(__name__)

if __name__ != '__main__':
    gunicorn_logger = logging.getLogger('gunicorn.error')
    app.logger.handlers = gunicorn_logger.handlers
    app.logger.setLevel(gunicorn_logger.level)

catalogfile = 'model/model-catalog.ttl'

@app.route('/')
def modelById():
    app.logger.debug('Reading graph from file')
    g=rdflib.Graph()
    g.parse(catalogfile, format='turtle')
    return Response(g.serialize(format='turtle', encoding='utf8'), mimetype='text/turtle')

@app.route('/ready', methods=['GET'])
def isReady():
    return "OK"

@app.route('/ping', methods=['GET'])
def isAlive():
    return "OK"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=config.PORT, debug=config.DEBUG_MODE)
