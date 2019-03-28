# -*- coding: utf-8 -*-
__operators = ('+', '-', '/', '//', '*', '**', '%')


def calculator():
    x = eval(input())
    operator = eval(input())
    y = eval(input())

    print(str(x) + operator + str(y))

    # your code here
    rezultat = 0
    if(operator=='+'):
        rezultat = x+y
    elif(operator=='-'):
        rezultat = x-y
    elif(operator=='/'):
        rezultat= x/y
    elif (operator == '//'):
        rezultat =  x // y
    elif (operator == '*'):
        rezultat = x * y
    elif (operator == '**'):
        rezultat = x**y
    elif (operator == '%'):
        rezultat = x%y
    else:
        rezultat = "Taa operacija nemoze da se izvrzhi"
    print(rezultat)
    return rezultat


if __name__ == "__main__":
    calculator()