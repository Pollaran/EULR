sum = 0
for x in range(1000):
  flag = 0
  if x % 3 == 0:
    flag = flag + 1
  if x % 5 == 0:
    flag = flag + 1
  if flag > 0:
    sum = sum + x

print(sum)
