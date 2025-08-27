def is_prime(n):
    # Prime numbers are greater than 1
    if n <= 1:
        return False
    
    # Check divisibility from 2 to sqrt(n)
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


# Test the function
# num = 29
num = int(input("Enter a number: "))
if is_prime(num):
    print(f"{num} is a prime number")
else:
    print(f"{num} is not a prime number")
