import pytest


def test_lambda_handler():
    from src.main import lambda_handler

    event = None
    context = None

    handler_return = lambda_handler(event, context)
    expected_return = 'Hello'

    #### Começa os testes

    assert isinstance(handler_return, str)
    assert handler_return == expected_return

def test_par():
    from src.main import par

    handler_return = par()
    expected_return = bool(handler_return%2==0)

    assert expected_return == True