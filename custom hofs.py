def map(func, lisy)-> list:
  output = []
  for item in lisy:
    output.append(func(item))
  return output

x = [2,3,5,7,1.5,1000]

square = lambda x : x*x*2
map(square, x)
print(list(map(square, x)))