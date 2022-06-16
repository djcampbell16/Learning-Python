# Binary to Decimal and Back Converter
# Develop a converter to convert a decimal number to binary or a binary number to its decimal equivalent.
import unittest

bin_list = ['0', '1', '1010', '1100100', '11001101', '1111100111', '1111']
int_list = [0, 1, 10, 100, 205, 999, 15]

def int_to_bin(num):
    """ converts int to equivalent binary representation as a string

    :param num: integer number to convert
    :return: string of binary value
    """
    isZero = num == 0

    converted_binary = ''

    while num > 0:
        # Whole part remaining
        quotient = int(num/2)
        # remainder will either be 1 or 0 and added to binary string
        remainder = num % 2
        # add remainder to start of string
        converted_binary = str(remainder) + converted_binary

        # Update integer to be the whole part remaining
        num = quotient

    # Return string representing the integer in binary
    if isZero:
        return "0"
    else:
        return converted_binary

def bin_to_int(bin):
    """ converts string representation of a binary number to it int value

    :param bin: string of binary value to convert
    :return: integer value of binary input
    """
    integer = 0
    count = 0

    for digit in bin:
        integer += int(digit) * (2**(len(bin)-count-1))
        count += 1
    return integer

class binaryIntTests(unittest.TestCase):
    def testIntToBin(self):
        for num in range(len(int_list)):
            with self.subTest():
                expectedBin = bin_list[num]
                message = "Expected int_to_bin({intnum}) to return {result}".format(intnum=str(int_list[num]), result=bin_list[num])
                self.assertEqual(int_to_bin(int_list[num]), expectedBin, message)

    def testBinToInt(self):
        for num in range(len(bin_list)):
            with self.subTest():
                expectedInt = int_list[num]
                message = "Expected bin_to_int({binary}) to return {result}".format(binary=bin_list[num], result=str(int_list[num]))
                self.assertEqual(bin_to_int(bin_list[num]), expectedInt, message)

def main():
    unittest.main()

if __name__ == '__main__':
    main()