square = lambda x : x*x
print(square(180))

x = [2,3,5,7,1.5,1000]

for idx, number in enumerate(x):
  x[idx] = number * number

print(x)

multiply = lambda x , y: x*y
print(multiply(2,3))