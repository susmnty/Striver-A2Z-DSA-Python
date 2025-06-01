from math import *
from collections import *
from sys import *
from os import *

## Read input as specified in the question.
## Print output as specified in the question.
def fibonacci(n):
    if n == 1 or n == 2:
        return 1

    a, b = 1, 1
    for i in range(3, n + 1):
        a, b = b, a + b
    return b

# Read input
n = int(input())

# Print output
print(fibonacci(n))