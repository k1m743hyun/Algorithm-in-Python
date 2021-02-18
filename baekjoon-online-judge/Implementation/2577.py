a = int(input())
b = int(input())
c = int(input())

li = list(str(a * b * c))

for i in range(10):
  print(li.count(str(i)))