def prime_checker(number):
    counter = 0
    for n in range(1, number + 1):
        if number % n == 0:
            counter += 1
    if counter == 2:
        print("It's a prime number.")
    else:
        print("It's not a prime number.")

n = int(input("Check this number: "))
prime_checker(number=n)

