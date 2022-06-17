# Projects from the following link
# https://github.com/karan/Projects

# Start with a number n > 1. Find the number of steps it takes to reach one using the following process:
# If n is even, divide it by 2. If n is odd, multiply it by 3 and add 1.

def runCollatz(n):
    if n <= 1:
        return "Please run again... n must be greater than 1"
    else:
        steps = 1
        currentNum = n

        while currentNum != 1:
            print("Step " + str(steps) + " --- " + str(currentNum))
            if currentNum % 2 == 0:
                currentNum = int(currentNum/2)
            else:
                currentNum = int((currentNum*3) + 1)

            steps += 1

        print("Step " + str(steps) + " --- " + str(currentNum))
        print("\nTotal Steps Needed: " + str(steps))


def main():
    n = 17
    runCollatz(n)

if __name__ == '__main__':
    main()