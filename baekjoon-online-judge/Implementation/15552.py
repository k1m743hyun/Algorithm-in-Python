import sys;

n = int(float(sys.stdin.readline()))

for i in range(n):
  a, b = map(int, sys.stdin.readline().split())
  print(a + b)