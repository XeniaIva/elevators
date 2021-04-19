def read_command():
    """ Read a command from user in format <source> <action> <value> """
    pass


def print_greeting():
    """ Say hello to user """
    pass


def process_command():
    """ Perform actions based on user's command """
    pass


def main():
    print_greeting()
    user_command = read_command()
    while(user_command is not None):
        process_command()
        user_command = read_command()


if __name__ == '__main__':
    main()