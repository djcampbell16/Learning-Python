# Projects from the following link
# https://github.com/karan/Projects

# Code Block 2 - Prime Factorization
# Have the user enter a number and find all Prime Factors (if there are any) and display them.'

def isPrime(number):
    if number >= 2:
        for n in range(2, number):
            if number % n == 0:
                return False
        return True
    else:
        return False



def primeFactorization(number):
    prime_factors = []
    for num in range(1, number):
        if number % num == 0 and isPrime(num):
            prime_factors.append(num)
    return 'The prime factors of {number} are {primes}'.format(number=number, primes=prime_factors)