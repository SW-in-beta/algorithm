def solution(numbers):
    res = ''.join(sorted(map(str, numbers), reverse=True, key=lambda a: ((a * 4)[:4], len(a))))
    return '0' if res[0] == '0' else res
    