def solution(s):
    return len([i for i in s.lower() if i == 'p']) == len([j for j in s.lower() if j == 'y'])