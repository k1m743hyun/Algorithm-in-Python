li = []

while True:
    try:
        a, b = map(int, input().split())
        li.append((a, b))
    except:
        break
    
for i in li:
    print(sum(i))