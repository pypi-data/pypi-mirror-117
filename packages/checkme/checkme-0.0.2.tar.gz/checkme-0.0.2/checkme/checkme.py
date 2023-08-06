import platform

def is_it(os):
    if platform.system().lower() == os:
        return True
    else:
        return False
