def solution(arr):
    answer = []
    flag = 0
    for i in range(len(arr)):
        if flag == 0:
            answer.append(arr[i])
        
        if i == len(arr) - 1:
            break
            
        if arr[i] == arr[i + 1]:
            flag = 1
        else:
            flag = 0
        
    return answer