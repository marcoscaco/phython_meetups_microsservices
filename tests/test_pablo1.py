def test_serv():
    from src.pablo1 import serv

    serv_return = serv()
    expect_return = "Teste feito com sucesso"

    # Os testes
    assert isinstance(serv_return, str)
    assert serv_return == expect_return
