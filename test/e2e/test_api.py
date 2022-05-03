import json

from src.entrypoints.api.app import app


def test_root_route():
    response = app.test_client().get("/")
    assert response.data.decode("utf-8") == "Hello there"


def test_add_endpoint_int_and_float(get_test_client_with_context):

    data = {"number1": 20, "number2": 10.5}

    response = get_test_client_with_context.get("/add", query_string=data)
    res = json.loads(response.data.decode("utf-8"))
    assert response.status_code == 200
    assert res == {"result": 30.5}


def test_add_endpoint_int_and_list(get_test_client_with_context):
    data = {"number1": 20, "number2": []}

    response = get_test_client_with_context.get("/add", query_string=data)
    assert response.status_code == 400


def test_subtract_endpoint_int_and_float(get_test_client_with_context):
    data = {"number1": 20, "number2": 10.5}

    response = get_test_client_with_context.get("/subtract", query_string=data)
    res = json.loads(response.data.decode("utf-8"))
    assert response.status_code == 200
    assert res == {"result": 9.5}


def test_subtract_endpoint_int_and_tuple(get_test_client_with_context):
    data = {"number1": 20, "number2": ()}

    response = get_test_client_with_context.get("/subtract", query_string=data)
    assert response.status_code == 400


def test_multiply_endpoint_int_and_float(get_test_client_with_context):
    data = {"number1": 20, "number2": 1.0}

    response = get_test_client_with_context.get("/multiply", query_string=data)
    res = json.loads(response.data.decode("utf-8"))
    assert res == {"result": 20.0}
    assert response.status_code == 200


def test_multiply_endpoint_int_and_string(get_test_client_with_context):
    data = {"number1": 20, "number2": "asdasds"}

    response = get_test_client_with_context.get("/multiply", query_string=data)
    assert response.status_code == 500


def test_divide_endpoint_int_and_zero(get_test_client_with_context):
    data = {"number1": 20, "number2": 0}

    response = get_test_client_with_context.get("/divide", query_string=data)
    assert response.status_code == 500
