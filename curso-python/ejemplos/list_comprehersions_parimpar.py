def run():
    squares = [(i,"Event") if i%2==0 else (i,"Odd") for i in range (1,10)]
    print(squares)

if __name__ == '__main__':
    run()