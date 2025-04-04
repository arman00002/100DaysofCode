print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")
bill=0
if size=='s' or size=='S':
    bill+=15
    if pepperoni=='y' or pepperoni=='Y':
        bill+=2
    if extra_cheese=='y' or extra_cheese=='Y':
        bill+=1
elif size=='m' or size=='M':
    bill+=20
    if pepperoni=='y' or pepperoni=='Y':
        bill+=3
    if extra_cheese=='y' or extra_cheese=='Y':
        bill+=1
elif size=='l' or size=='L':
    bill+=25
    if pepperoni=='y' or pepperoni=='Y':
        bill+=3
    if extra_cheese=='y' or extra_cheese=='Y':
        bill+=1
print(f"Your final bill is: ${bill}.")
