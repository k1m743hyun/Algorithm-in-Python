n = int(input())
li = list(map(int, input().split()))

m = max(li)
for idx, val in enumerate(li):
  li[idx] = val / m * 100

print(sum(li) / n)