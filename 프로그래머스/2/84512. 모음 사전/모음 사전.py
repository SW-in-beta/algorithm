"""
AAAA일때 뒤에 나올 수 있는 가지 수 5 ** 1 + 5 ** 0개
AAA일 때 뒤에 나올 수 있는 가지 수 5 * 5 + 5 + 1개
AA일 때 뒤에 나올 수 있는 가지 수  5 * 5 * 5 + 5 * 5 + 5 + 1
A일 때 뒤에 나올 수 있는 가지 수 5 ** 3 + 5 ** 2 + 5 ** 1 + 5 ** 0

결국 첫째자리 * (5 ** 3 + 5 ** 2 + 5 ** 1 + 5 ** 0)
둘째자리 * ()
"""
index = dict((a, i) for i, a in enumerate('AEIOU'))
def solution(word):
    seq = 0
    i = 4
    for w in word:
        seq += index[w] * sum(5 ** j for j in range(i + 1)) + 1
        i -= 1
    return seq