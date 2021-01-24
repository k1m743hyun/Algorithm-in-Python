def solution(n, lost, reserve):
    lost, reserve = set(lost) - set(reserve), set(reserve) - set(lost)
    n -= len(lost)
    for k in lost:
        if k - 1 in reserve:
            reserve.remove(k - 1)
            n += 1
        elif k + 1 in reserve:
            reserve.remove(k + 1)
            n += 1
    return n