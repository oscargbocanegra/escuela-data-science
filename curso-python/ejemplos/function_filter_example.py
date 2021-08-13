def run():
    my_list = [1,4,5,6,9,13,19,21]

    add = list(filter(lambda x: x%2 !=0, my_list))
    print(add)

if __name__ == '__main__':
    run()