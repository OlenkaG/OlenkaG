
    def merge(dict_1, dict_2):
       
        crushed_dict = dict_1.copy()
        crushed_dict.update(dict_2)
        return crushed_dict


    def dict_creator(user_input_1, user_input_2):
        dictionary_1 = {}
        dictionary_2 = {}
        id_counter = 0

        for char_1 in user_input_1:
            id_counter += 1
            dictionary_1["ID " + str(id_counter)] = char_1
        # тоже самое и со вторім словарем
        for char_2 in user_input_2:
            id_counter += 1
            dictionary_2["ID " + str(id_counter)] = char_2

        print(merge(dictionary_1, dictionary_2))



    dict_creator(input("Dictionary 1: "), input("Dictionaryv2: "))
