def lambda_handler(event, context):
    return 'Hello World'



if __name__ == '__main__':
    event = None
    context = None

    print(lambda_handler(event=event,context=context))