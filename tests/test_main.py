import pytest


def test_lambda_handler():
    from src.main import lambda_handler

    event = None
    context = None

    handler_return = lambda_handler(event, context)

    expected_return = 3

    #### Começa os testes

    assert isinstance(handler_return, int)
    assert handler_return == expected_return

