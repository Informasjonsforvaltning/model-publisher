import requests
import schemathesis

with open('model-catalog.yaml') as f:
    schema = schemathesis.from_file(f, base_url='http://localhost:8080')

@schema.parametrize()
def test_no_server_errors(case):
    # `requests` will make an appropriate call under the hood
    response = case.call()  # use `call_wsgi` if you used `schemathesis.from_wsgi`
    # You could use built-in checks
    case.validate_response(response)
    # Or assert the response manually
    assert response.status_code < 500
