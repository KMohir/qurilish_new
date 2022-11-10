from curses import wrapper


def deco(func):
    def start(*args,**kwargs):
        print('1111')
        func(*args,*kwargs)
        print('33333333333')
    deco.__name__=func.__name__
    deco.__doc__=func.__doc__
    return start

def hello():
    print('222222222222222')

a=deco(hello)
print(hello.__name__)

a()
wrapper()