import start


class User:
    def __init__(self):
        self.name = ''
        self.password = ''
        self.age = 1
        self.gender = 0
        self.net_address = '1:2'
        self.address = ''


def add_user(user_input):
    user = start.user()
    user.name = user_input.name
    user.password = user_input.password
    user.age = user_input.age
    user.gender = user_input.gender
    user.net_address = user_input.net_address
    user.address = user_input.address

    session = start.Session()

    session.add(user)

    session.flush()


def test_add():
    user = User()
    add_user(user)


def get_user(name):
    session = start.Session()
    user = start.user
    print(user)
    result = session.query(user).filter(user.name == name).one()
    print(result)
    return result


def test_get():
    user = get_user("chenyi")
    print(user.name, user.password)


test_get()
