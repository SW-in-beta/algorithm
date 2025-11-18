"""
+랑 -밖엥 벗다. 그리고 결합
arr의 길이 항상 홀수
숫자는 자연수

뭐를 늘려가면서 해야하나
투포인터 해야할 것 같은 느낌
i부터 j까지의 최댓값 최솟값 남겨서
최대 최소를 동적으로 계산해서 갖고있으면?

시간 복잡도를 계산해보자.
간격을 1, 2, 3, 4, ... 201
간격마다 업데이트 해주는데, 시작 숫자는 202 - i번
그리고 시작 숫자마다 확인하는 수는 또 i-1 번
대충 많아봐야 i**3이고 201이니까, 통과할 수 있을 것 같은데
숫자와 연산자는 어떻게 관리하는게 나으려나
숫자 따로 연산자 따로 관리하자.
"""

from collections import namedtuple
from operator import add, sub
operators = {'+': add, '-': sub}
DP = namedtuple('DP', ['max', 'min'])
INF = float('inf')

def solution(arr):
    nums = []
    opers = []
    for i, e in enumerate(arr):
        if i % 2:
            opers.append(e)
        else:
            nums.append(int(e))
            
    # dp가 2차원 배열이여야 한다. start, end 기준으로 가장 max
    dp = [[None for _ in range(len(nums))] for _ in range(len(nums))]
    for i, n in enumerate(nums):
        dp[i][i] = DP(n, n)
        
    for step in range(1, len(nums)):
        for start in range(len(nums) - step):
            end = start + step
            max_res, min_res = -INF, INF
            
            for mid in range(start, end):
                a = dp[start][mid]
                oper = opers[mid]
                b = dp[mid + 1][end]
                # 최댓값 = 덧셈이면 max + max, 뺄셈이면 max - min
                # 최솟값 = 덧셈이면 min + min, 뺄셈이면 min - max
                o = operators[oper]
                if oper == '+':
                    max_res = max(max_res, o(a.max, b.max))
                    min_res = min(min_res, o(a.min, b.min))
                else:
                    max_res = max(max_res, o(a.max, b.min))
                    min_res = min(min_res, o(a.min, b.max))
            dp[start][end] = DP(max_res, min_res)
    return dp[0][len(nums) - 1].max