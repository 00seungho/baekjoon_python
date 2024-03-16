def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def divide(a,b):
    return a/b
def multiply(a,b):
    return a*b
a = input()
c = input()
b = input()
if c == "+":
    print(add(a,b))
if c == "-":
    print(subtract(a,b))
if c == "/":
    print(divide(a,b))
if c == "*":
    print(multiply(a,b))
