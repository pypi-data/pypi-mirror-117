from . import another_process


def get_message():
    return "Hello World!"


def message():
    '''checking a processoutcome before return'''
    if another_process.get_decision():
        print(get_message())
    return True


if __name__ == '__main__':
    message()
