# Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:
# 1 2 3 5 8 13 21 34 55 89 ...
# By considering the terms in the Fibonacci sequence who values do not exceed four million, find the sum of the even-valued terms
# find the sum of the even-valued terms

MAX = 4000000
array = [1, 2, 3, 5]
sum = 2

while  sum < MAX:
  # Current working array
  print("New itteration: "
       + str(array[0]) + " " + str(array[1]) + " " + str(array[2]) + " " + str(array[3]))
  # If the next number is even add it to the sum
  if (array[2] + array[3]) % 2 == 0:
    sum = (array[2] + array[3]) + sum
    print("New sum: " + str(sum)) # Test code
  # Reset array for next itteration
  array[0] = array[3]            # 5 2 3 5
  array[1] = array[2] + array[3] # 5 8 3 5
  array[2] = array[0] + array[1] # 5 8 13 5
  array[3] = array[1] + array[2] # 5 8 13 21

print("Final sum: " + str(sum))
