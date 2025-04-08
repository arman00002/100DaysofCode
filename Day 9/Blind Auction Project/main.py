# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary
import art
data={}
print(art.logo)
def bidding():
    name=input("Enter Name:")
    bid=int(input("Enter bid price:"))
    data[name]=bid
def call():
    while True:
        bidding()
        play=input("Enter yes if there are other bidders\n").lower()
        if play=='yes':
            print('\n'*20)
        else:
            break
def result():
    max=0
    k=''
    for key in data:
        if data[key]>max:
            k=key
    print(f"The winner is {k} with a bid of ${data[k]}")
def auction():
    call()
    result()

auction()