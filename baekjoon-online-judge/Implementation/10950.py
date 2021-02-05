n = int(input())

results = list(sum(map(int, input().split())) for _ in range(n))

for res in results:
  print(res)