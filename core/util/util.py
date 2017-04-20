import random

def randstring(length=10):
    valid_letters='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    return ''.join((random.choice(valid_letters) for i in xrange(length)))