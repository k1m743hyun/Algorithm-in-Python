n = int(input())
times = map(int, input().split())

result = 0
temp = 0

for time in sorted(times):
  temp += time
  result += temp

print(result)