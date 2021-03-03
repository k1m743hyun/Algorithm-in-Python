def solution(numbers):
    answer = []
    for idx_i, val_i in enumerate(numbers):
        for idx_j, val_j in enumerate(numbers):
            if idx_i == idx_j:
                continue
            answer.append(val_i + val_j)
    return sorted(set(answer))