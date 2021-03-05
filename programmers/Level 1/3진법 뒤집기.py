import math

def solution(n):
    numList = []
    for _ in range(int(math.log10(n) / math.log10(3)) + 1):
        numList.append(int(n % 3))
        n /= 3
    answer = 0
    for idx, val in enumerate(numList[::-1]):
        answer += val * math.pow(3, idx)
    return answer