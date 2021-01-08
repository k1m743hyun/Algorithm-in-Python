n, k = map(int, input().split())

cashes = list()

for i in range(n):
    cashes.append(int(input()))

result = 0

for cash in cashes[::-1]:
    result += k // cash
    k = k % cash

print(result)