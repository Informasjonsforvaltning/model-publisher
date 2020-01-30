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

## Running the API in Docker

To build and run the api in a Docker container:
```
% docker build -t digdir/model-publisher:latest .
% docker run -p 5000:5000 -d digdir/model-publisher:latest
```

## Test the endpoint

Regardless if you run the app via Docker or not, in another terminal:
```
curl -H "Accep: text/turtle" "http://localhost:5000/"
```
