import random
import string


def lets_make_a_list():

    numbers_1 = [str(random.randrange(1, 9999999, 1))]
    numbers_2 = [str(random.randrange(1, 9999999, 1))]

    a = list(random.choice(numbers_1))
    b = list(random.choice(numbers_2))
    print(a)
    print(b)

    def value():

        same_values = list(set(a) & set(b))
        print("\033[035m",same_values)

    value()


lets_make_a_list()