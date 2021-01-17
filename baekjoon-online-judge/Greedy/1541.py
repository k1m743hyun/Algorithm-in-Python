n = input().split('-')

res = []
for i in range(len(n)):
  if i == 0:
    res.append(sum(map(int, n[i].split('+'))))

  else:
    res.append(-sum(map(int, n[i].split('+'))))

print(sum(res))