#!/usr/bin/env python

"""
Generate random numbers from the interval [1, 10]
in a non-deterministic way
"""

import random

UPPER = 10


def main():
    for _ in range(10):
        print random.randint(1, UPPER), 
    print

#############################################################################

if __name__ == "__main__":
    main()
