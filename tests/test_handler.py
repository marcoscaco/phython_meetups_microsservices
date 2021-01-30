import pytest


def test_lambda_handler():
    from src.handler import lambda_handler

    event = None
    context = None

    handler_return = lambda_handler(event, context)
    expected_return = f"Recebemos o evento {event} no contexto {context}"

    # Início dos testes
    assert isinstance(handler_return, str)
    assert handler_return == expected_return
