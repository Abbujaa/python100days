from functools import reduce

x = [2, 3, 5, 7, 1.5, 1000]

is_even = lambda x:x%2==0
print(list(filter(is_even, x)))

for i in x:
  print(i)

print(x)

sum_up = lambda a, b: a + b

x = reduce(sum_up, x)


print(x)