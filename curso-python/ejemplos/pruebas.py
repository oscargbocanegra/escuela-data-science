def fix_me(my_list):
    if len(my_list) % 2:  # imperative code
        print("Ok la lista ingresa por if")
        new_list = []
        for item in my_list:
            for element in item:
                new_list = new_list.append(element)
    else:  # functional code
        new_list = [element for item in my_list for element in item]
        new_list.sort(reverse = True, key = lambda x: x % 5 + x / (max(new_list)*2))
        return print(new_list)


fix_me([ [ 3, 4 ], [ 2, 6 ] ])

