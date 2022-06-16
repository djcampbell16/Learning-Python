# Projects from the following link
# https://github.com/karan/Projects

# Code Block 3 - Next Prime Number
# Have the program find prime numbers until the user chooses to stop asking for the next one.
def nextPrimeNumber():
    valid_responses = ['Y', 'N']
    finding_next_prime = True
    currentNum = 1
    while finding_next_prime:
        valid_response = False
        attempts = 0

        while not valid_response:
            response = input('Would you like to find the next prime number? Enter Y or N: ')
            if response.upper() not in valid_responses:
                attempts += 1
                if attempts == 3:
                    return 'Maximum attempts exceeded'
            else:
                valid_response = True
                if response.upper() == 'N':
                    finding_next_prime = False


        foundNextPrime = False
        while not foundNextPrime:
            if isPrime(currentNum):
                print('The number {number} is the next prime number\n'.format(number=currentNum))
                foundNextPrime = True
            currentNum += 1




# if __name__ == '__main__':
#
#     print("\nThis is Code Block #3\n")
#     nextPrimeNumber()