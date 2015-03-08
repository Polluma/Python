__author__ = 'Marcin'


def simple_func(x):
    print(x)
    return


class Koko:

    def __init__(self,x):
        self.number = x

    def print_number(self):
        print(self.number)

if __name__ == '__main__':
    print('Hello')
    x = input('Type number\n')
    print(x)
    print(type(x))
    msg = input("Enter your name\n")
    print("Your name is %s" % (msg))