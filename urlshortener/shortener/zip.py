import random
import string

def get_zipped():
    return ''.join(random.sample(string.ascii_letters+string.digits, 5))
