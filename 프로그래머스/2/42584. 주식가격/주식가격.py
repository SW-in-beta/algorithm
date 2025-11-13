"""
스택에 넣어가면서
"""
def solution(prices):
    answer = [0] * len(prices)
    stack = []
    for i, p in enumerate(prices):
        while stack and prices[stack[-1]] > p:
            ni = stack.pop()
            answer[ni] = i - ni
        stack.append(i)
        
    for i in stack:
        answer[i] = len(prices) - i - 1
        
    return answer