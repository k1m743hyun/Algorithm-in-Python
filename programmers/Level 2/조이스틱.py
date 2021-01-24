def solution(name):
    count = [min(ord(i) - ord('A'), ord('Z') - ord(i) + 1) for i in name]
    answer = 0
    index = 0
    
    while True:
        answer += count[index]
        count[index] = 0
        if sum(count) == 0:
            return answer
        
        left = 1
        while count[index - left] == 0:
            left += 1
        
        right = 1
        while count[index + right] == 0:
            right += 1
        
        answer += left if left < right else right
        index += -left if left < right else right