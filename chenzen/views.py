from chenzen import chenzen


@chenzen.route('/')
def index():
    return 'Testing this app!'
