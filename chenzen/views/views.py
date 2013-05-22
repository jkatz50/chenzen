from chenzen import chenzen


@chenzen.route('/')
def index():
    return 'Testing this app!'

@chenzen.route('/login')
def login():
	pass

@chenzen.route('/register')
def register():
	pass
	