a = int(input("\033[034m""Введите первое число: " ))
b = int(input("Введите второе число: " ))
c = int(input("Введите шаг: " ))
def compare(a, b):
    while b>a:
        a += c
        if b>a:
            print("\033[0m" "Not yet, a = ",(a))
        else:
            print ("\033[0m\033[36m""Finally,a = ", (a))

compare(a,b)