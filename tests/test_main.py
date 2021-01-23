import pytest

def test_lambda_handler():
    from src.main import lambda_handler
    

    event = None
    context = None

    handler_return = lambda_handler(event,context)
    expected_return = "Hello World"
    assert isinstance(handler_return, str)
    assert handler_return == expected_return
