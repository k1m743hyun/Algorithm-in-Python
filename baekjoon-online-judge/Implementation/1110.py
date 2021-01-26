a = input()

if len(a) == 1:
    a = '0' + a

res = list()
res.append(a)

while True:
    li = list(res[-1])
    temp = li[-1] + str(sum(map(int, li)))[-1]
    if temp == res[0]:
        break
    res.append(temp)

print(len(res))