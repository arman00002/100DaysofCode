import art
def add(n1, n2):
    return n1 + n2
def sub(n1,n2):
    return n1-n2
def mul(n1,n2):
    return n1*n2
def div(n1,n2):
    return n1/n2
dict={"+":add,"-":sub,"*":mul,"/":div}

def calculator():
    print(art.logo)
    cont=True
    n1 = float(input("Enter First number"))
    while cont:
        for i in dict:
            print(i)
        op=input("Enter operator")
        n2=float(input("Enter Second number"))
        result=(dict[op](n1,n2))
        choice=(f'Type "y" to continue calculation with {result}, type "n" to start new calculation')
        if choice=="y":
            num1=result
        else:
            cont=False
            print("\n"*20)
            calculator()

calculator()