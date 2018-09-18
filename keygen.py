import string
import random

def random_char(y):
       return ''.join(random.choice(string.ascii_letters) for x in range(y))


def gen1():
    word = random_char(4)
    first = word.upper()
    key1 =""
    num = 0
    for i in first:
        num += ord(i)
    if num % 5 == 0:
        return first
    else:
        gen1()

def gen2():
    word = random_char(4)
    second = word.upper()
    num = 0
    for i in second:
        num += ord(i)
    if num % 11 == 0:
        return second
    else:
        gen2()
def Main():
    one = gen1()
    two = gen2()
    zero = 'PASGEN-'
    while True:
        if (one == None or two == None):
            one = gen1()
            two = gen2()
        else:
            print "Here for you a new brand LicenseKey: ",zero+str(one)+str(two)
            break


Main()
