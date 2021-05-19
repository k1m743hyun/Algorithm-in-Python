def solution(phone_number):
    return ''.join([v if i > len(phone_number) - 5 else '*' for i, v in enumerate(phone_number)])