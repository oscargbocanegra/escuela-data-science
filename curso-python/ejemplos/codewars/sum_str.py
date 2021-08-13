"""
Create a function that takes 2 positive integers in form of a string as an input, 
and outputs the sum (also as a string):
Example: (Input1, Input2 -->Output)
"""
def sum_str(a, b):
    if a == "":
        a = 0
    elif b == "":
        b = 0
    elif a == "" and b == "":
        a = 0
        b = 0
    return print(f' "{(a)}" , "{(b)}" --> "{str(int(a) + int(b))}"' )

if __name__ == '__main__':
    sum_str("", "5")