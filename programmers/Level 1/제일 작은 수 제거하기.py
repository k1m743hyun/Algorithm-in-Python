def solution(arr):
    minVal = min(arr)
    answer = [i for i in arr if i != minVal]
    return answer if len(answer) != 0 else [-1]