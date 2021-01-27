a = int(input())
b = list(input())
for i in b[::-1]:
    print(a * int(i))
print(a * int(''.join(b)))