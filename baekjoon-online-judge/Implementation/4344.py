n = int(input())

for i in range(n):
  li = list(map(int, input().split()))
  avg = sum(li[1:]) / li[0]
  cnt = 0
  for j in li[1:]:
    if j > avg:
      cnt += 1
  print("{:.3f}%".format(cnt / li[0] * 100))