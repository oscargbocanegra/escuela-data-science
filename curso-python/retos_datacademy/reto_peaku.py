def fix_me(my_list):

    if len(my_list) % 2:  # imperative code
        new_list = []
        for item in my_list:
            for element in item:
                new_list = new_list.append(element)
    else:  # functional code
        new_list = [element for item in my_list for element in item]
        #print(new_list)

    # sorting hierarchy:
    #   1. desc by x % 5
    #   2. desc by x
    #new_list.sort(reverse=True, key=lambda x: x % 5 + x/(max(new_list)*2))
    new_list.sort(reverse=True, key=lambda x: x % 5 + x/(max(new_list)*2))
    print(new_list)



fix_me([ [ 3, 4 ], [ 2, 6 ] ])

# Salida esperada:
# [4, 3, 2, 6]
