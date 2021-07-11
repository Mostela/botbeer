#  Copyright (c) 2021.
#  Date: 2021 / 6 / 19
#  Github: https://github.com/mostela
import random
import string


def random_device():
    return random.choice(string.ascii_uppercase + string.digits)
