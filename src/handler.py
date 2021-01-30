def lambda_handler(event, context):
    """

    :param event: Evento vindo da AWS
    :param context: Contexto de execução da função
    :return: Uma string que informa o evento e o contexto
    """
    return f'Recebemos o evento {event} no contexto {context}'


if __name__ == '__main__':
    event = None
    context = None

    print(lambda_handler(
        event=event,
        context=context
    ))
