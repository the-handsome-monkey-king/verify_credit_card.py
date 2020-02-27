#!/usr/bin/env python
"""verify_credit_card.py

Verify a credit card number using the Luhn Algorithm.
This will not test whether a credit card is valid or not, but
will test whether the input number adheres to accepted checksum
creation against non-malicious mistakes."""

__author__ = "Ryan Morehouse"
__license__ = "MIT"

import sys

def main():
    try:
        cc = (int)(sys.argv[1])
    except(ValueError, IndexError):
        print("Usage: verify_cc_with_lun.py [n]")
        print("[n] = credit card number (without spaces)")
        sys.exit(1)

    # get number as array of ints
    num_array = (list)(str(cc))
    for i in range(len(num_array)):
        num_array[i] = (int)(num_array[i])
    
    # reverse list
    num_array.reverse()

    # double every other digit after 0
    for i in range(len(num_array)):
        if i % 2 != 0:
            digit = i*2
            if digit > 9:
                digit -= 9
            num_array[i] = digit

    sum = 0
    for digit in num_array:
        sum += digit

    if sum % 10 == 0:
        print("Credit card is valid against Luhn's Algorithm.")
    else:
        print("Credit card is invalid against Luhn's Algorithm.")

if __name__ == "__main__":
    main()
