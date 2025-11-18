"""
거쳐간 숫자의 합이 가장 큰 경우
높이는 1이상 500이하
숫자는 0이상 9,999 이하의 정수
각 자리마다, 자기를 거쳤을 때 가장 큰 합을 갖고 있으면 될 것 같은데
triangle 자체를 dp배열로 확인해도 되나?
밑 층에서 윗 층을 확인하면 예외조건도 있고 해서 귀찮을 것 같은데 다만 triangle을 그대로 dp 배열로 활용할 수 있어서 공간적으로는 좋을 것 같다. 그냥 그렇게 하자
"""
def upper_index(r, c):
    return ((r-1, c + i) for i in (-1, 0) if 0 <= c + i < r)

def solution(triangle):
    for r, row in enumerate(triangle[1:], start=1):
        for c, col in enumerate(row):
            triangle[r][c] += max(triangle[ur][uc] for ur, uc in upper_index(r, c))
    return max(*triangle[-1])