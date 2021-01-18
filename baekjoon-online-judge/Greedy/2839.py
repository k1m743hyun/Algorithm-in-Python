n = int(input())

def calculator(n, res, i):
  res += n // i
  n = n % i
  return n, res
  
res = 0
n, res = calculator(n, res, 5)

if n == 0:
  print(res)

else:
  if res > 0 and (n % 3) == 1:
    n, res = calculator(n + 5, res - 1, 3)
    print(res)

  elif res > 1 and (n % 3) == 2:
    n, res = calculator(n + 10, res - 2, 3)
    print(res)
  
  else:
    n, res = calculator(n, res, 3)

    if n == 0:
      print(res)

    else:
      print(-1)