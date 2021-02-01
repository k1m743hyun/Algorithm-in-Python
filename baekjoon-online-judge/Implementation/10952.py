li = []

while True:
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        break
    li.append((a, b))
    
for i in li:
    print(sum(i))