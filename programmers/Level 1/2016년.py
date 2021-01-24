def solution(a, b):
    dom = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    dow = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]
    
    sum = 0
    for i in range(a - 1):
        sum += dom[i]
    sum += b
    
    return dow[(sum + 4) % 7]