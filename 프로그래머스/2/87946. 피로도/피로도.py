"""
던전의 개수가 1이상 8이하 밖에 없다.
전부 다 돌 수 있겠는데?
"""
from itertools import permutations
def solution(k, dungeons):
    cnt = 0
    for ds in permutations(dungeons):
        local_k = k
        for i in range(len(ds) + 1):
            if i == len(ds):
                return i
            minimum, consume = ds[i]
            cnt = max(cnt, i)
            if local_k < minimum:
                break
            local_k -= consume
    return cnt