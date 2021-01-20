def main(dict):
    messages = dict.get('messages')

    if messages is None or messages[0] is None:
        return { 'error': "Invalid arguments. Must include 'messages' JSON array with 'value' field" }
    try:
        val = messages[0]['value']
    except KeyError:
        return { 'error': "Invalid arguments. Must include 'messages' JSON array with 'value' field" }

    for msg in messages:
        print(msg)

    return { 'msg': msg}
