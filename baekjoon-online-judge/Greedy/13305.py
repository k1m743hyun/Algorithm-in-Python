n = int(input())
distances = list(map(int, input().split()))
prices = list(map(int, input().split()))

minPrice = prices[0]
res = 0

for i in range(len(distances)):
  if minPrice > prices[i]:
    minPrice = prices[i]
  res += minPrice * distances[i]
  
print(res)