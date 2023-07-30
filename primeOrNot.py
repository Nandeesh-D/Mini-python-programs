def isPrime(n):
    if n<2:                  #if numbers less than 2
        return "Invalid input, enter a number greater than 1"
    for i in range(2, n):
        if n % i == 0:       #checking for factors
            return f"{n} is not prime"
    else:                    #if there are no factors b/w 2 and itself, it is prime
        print(f"{n} is a prime number")


n=int(input("Enter a number: "))
print(isPrime(n))