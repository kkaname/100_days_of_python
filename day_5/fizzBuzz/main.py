for num in range(1, 101):
    if (0 == num%3 and 0 == num%5):
        print("FizzBuzz.")
    elif (0 == num%3):
        print("Fizz")
    elif (0 == num%5):
        print("Buzz.")
    else:
        print(num)
