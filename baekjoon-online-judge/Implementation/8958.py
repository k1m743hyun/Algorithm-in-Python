n = int(input())

for i in range(n):
  res = 0
  continuous = 0
  for j in list(input()):
    if j == 'O':
      continuous += 1
    else:
      continuous = 0
    res += continuous
  print(res)