def add(x,y):
    sum =x+y
    print(a,"+",b,"=",sum)
def sub(x,y):
    s =x-y
    print(a,"-",b,"=",s)
def mul(x,y):
    m =x*y
    print(a,"*",b,"=",m)
def div(x,y):
    d =x+y
    print(a,"/",b,"=",d)
def floor_div(x,y):
    fd =x//y
    print(a,"//",b,"=",fd)
print("enter two number :")
a = int(input())
b = int(input())
print("Press + for addition")
print("Press - for substraction")
print("Pres * for multipliaction")
print("Press / for division")
print("Press // for floor_division")
ch = input()
if ch == "+":
    add(a,b)
elif ch=="-":
    sub(a,b)
elif ch == "*":
    mul(a,b)
elif ch == "/":
    div(a,b)
elif ch == "//":
    floor_div(a,b)
else:
    print("Invalid Choice")