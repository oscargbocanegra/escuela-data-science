"""
Your task is to make a function that can take any non-negative integer 
as an argument and return it with its digits in descending order. 
Essentially, rearrange the digits to create the highest possible number.
"""
def descending_order(num):
    num = (sorted(map(int, str(num)),reverse=True))
    num = int("".join(map(str, num)))
    return print(num)

if __name__ == '__main__':
    descending_order(42145)