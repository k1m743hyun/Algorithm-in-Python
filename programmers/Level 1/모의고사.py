def solution(answers):
    first_man = [1, 2, 3, 4, 5]
    second_man = [2, 1, 2, 3, 2, 4, 2, 5]
    third_man = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    scores = [0, 0, 0]
    
    for number, answer in enumerate(answers):
        if first_man[number % len(first_man)] == answer:
            scores[0] += 1
        if second_man[number % len(second_man)] == answer:
            scores[1] += 1
        if third_man[number % len(third_man)] == answer:
            scores[2] += 1
    
    return [index + 1 for index, score in enumerate(scores) if score == max(scores)]