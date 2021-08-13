def multi_table(number):
    return print('\n'.join(f'{i} * {number} = {i*number}' for i in range(1, 11)))
 

if __name__ == '__main__':
    multi_table(5)