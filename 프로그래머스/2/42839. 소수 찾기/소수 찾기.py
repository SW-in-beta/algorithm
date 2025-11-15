"""
다 붙여봤자 7자리 숫자.
7자리 수 이하의 소수를 다 구해볼까?
"""

from itertools import permutations
def solution(numbers):
    max_num = 10 ** len(numbers)
    is_prime = [False] * 2 + [True] * max_num
    for i in range(4, max_num, 2):
        is_prime[i] = False

    for i in range(3, int(max_num ** 0.5) + 1, 2):
        print(i)
        if not is_prime[i]:
            continue
        for j in range(i**2, max_num, i):
            is_prime[j]  = False
            
    s = set()
    cnt = 0
    for i in range(1, len(numbers) + 1):
        for n in permutations(numbers, i):
            n = int(''.join(n))
            if n in s:
                continue
            s.add(n)
            cnt += int(is_prime[n])
    return cnt