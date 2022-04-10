# The prime efactors of 13195 are 5, 7, 13, 29
# What is the largest prime factor of the number 600851475143

import math

MAX = 13195 # Constant cap
x = 0       # counter
prime_checker = 0

while x < MAX:
  # Check for divide by zero
  if x > 0:
    # Check if number is a factor
    if MAX % x == 0:
      # Check every number in range of the square root
      for n in range(int(math.sqrt(x))):
        prime_checker = 0
        if n > 0:
          if x % n == 0:
            prime_checker = prime_checker + 1
        if prime_checker > 0:
          print(str(x) + " is a prime factor!")
  x = x + 1
