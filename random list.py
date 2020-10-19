import random

a=int(input("Enter number FROM: " ))
b=int(input("Enter number TO: " ))



def lastfirst(mylist):
    mylist = random.sample(range(a, b+1),8)
    print("The list is:"+str(mylist))

    res = [ mylist[0], mylist[-1] ]
    print("\033[33m""The first and last element of list are : ",res)

lastfirst(mylist)
