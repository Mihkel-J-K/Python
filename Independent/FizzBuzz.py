def FizzBuzz(int: int):
    for i in range(1,int+1):
        print( ('Fizz'*(i % 3 == 0) + ('Buzz' * (i % 5 == 0))) or (i))

FizzBuzz(100)