def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    return a/b

def fact(n):
    if n <= 1:
        return 1
    return n * fact(n - 1)


if __name__ == '__main__' :

    # basic
    print("add 3+5 :",add(3,5))
    print("sub 3+5 :",sub(3,5))
    print("mul 3+5 :",mul(3,5))
    print("div 3+5 :",div(3,5))

    # fac
    print("factorial 5 :",fact(5))   # 5! = 120
    print("factorial 10 :",fact(10))  # 10! = 3628800


