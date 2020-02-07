# model-publisher

This service publishes a model catalog published by Digdir

The model is hand-coded in the file ./model/model-catalog.ttl
This model is transformed to the model-catalog standard and exposed through a simple REST endpoint.

## Running the API locally

You should work in a virtual environment. To do that, install [venv](https://docs.python.org/3/library/venv.html)

```
sudo apt-get install python3-venv
```
Create and activate your virtual environment
```
python3 -m venv .venv
source .venv/bin/activate
```
Install software and start the endpoint:
```
pip3 install --no-cache-dir -r requirements.txt
python3 app.py
```

## Running the API in a wsgi-server (gunicorn)
```
% cd src
% gunicorn wsgi:app --config=config.py
```
## Running the API in Docker

To build and run the api in a Docker container:
```
% docker build -t digdir/model-publisher:latest .
% docker run -p 8080:8080 -d digdir/model-publisher:latest
```

## Running tests
We use [pytest](https://docs.pytest.org/en/latest/) and [schemathesis](https://github.com/kiwicom/schemathesis) for testing the API against the [openAPI specification](./model-catalog.yaml).

To run the tests:
```
pytest test_api.py
```

## Test the endpoint

Regardless if you run the app via Docker or not, in another terminal:
```
% curl -H "Accept: text/turtle" "http://localhost:8080/model/person"
```
