import sys


def welcome():
    if len(sys.argv)>1:
        name=(sys.argv[-1])
    else:
        name="World"
    return(print("Hello "+ name +"!"))

welcome()
