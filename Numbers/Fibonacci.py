# Projects from the following link
# https://github.com/karan/Projects

# Code Block 1 - Fibonacci Sequence to the Nth digit
# Enter a number and have the program generate the Fibonacci sequence to that number or to the Nth number.'
def fibonacciSequence(numDigits):

    base_sequence = [0, 1]
    if numDigits < 0 or numDigits > 100:
        print("Please provide a number between 1 and 100")
        #return []
    elif numDigits == 0:
        return base_sequence[0]
    elif numDigits == 1:
        return base_sequence
    else:
        sequence = base_sequence
        for _ in range(numDigits-2):
            sequence.append(sequence[-1] + sequence[-2])
        return sequence
