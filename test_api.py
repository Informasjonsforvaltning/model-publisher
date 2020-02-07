import requests
import rdflib

def test_home_with_correct_accept_header():
    "GET request to url returns a 200"
    url = 'http://localhost:8080/'
    headers = {'Accept': 'text/turtle'}
    resp = requests.get(url, headers=headers)
    assert resp.status_code == 200
    assert len(resp.content) > 0

def test_that_model_parses_well():
    url = 'http://localhost:8080/'
    g=rdflib.Graph()
    assert g.parse(url, format='turtle')
    assert len(g) > 0

def test_ping():
    "Get request to /ping returns a 200"
    url = 'http://localhost:8080/ping'
    resp = requests.get(url)
    assert resp.status_code == 200

def test_ready():
    "Get request to /ready returns a 200"
    url = 'http://localhost:8080/ready'
    resp = requests.get(url)
    assert resp.status_code == 200
