from webhook import server


@server.route('/hello')
def hello():
    return 'Hello, World'
