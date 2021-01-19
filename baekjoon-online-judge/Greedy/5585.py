n = 1000 - int(input())

cashes = [500, 100, 50, 10, 5, 1]

count = 0
for cash in cashes:
  count += n // cash
  n = n % cash

print(count)