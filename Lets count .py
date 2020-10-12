a = input("Enter the phrase: ")
letter = input( "Which letter we are looking for: ")

s=0
for k in (a):
    if k==letter:
        s=s+1

if (s) > 0:
    print("\033[0m\033[34m""Ваше буква встречается",(s),"раз")
else:
    print("No such letter in the phrase")


