"""
물에 왜잠겨
아 왜 집이 있는 좌표가 1,1이야 0,0으로 하지

최단 경로가 아니라 최단 경로의 개수이다.
사실 최단 경로의 길이는 정해져 있다(m+n-2) -> 이건 중요하지 않은듯. 어차피 오른쪽과 아래로 밖에 못감

원래 갈 수 있는 경로에서 물웅덩이를 거쳐가는 경로를 빼야하나?
만약 그렇다면 어떤 물웅덩이부터 계산하느냐가 중요할 것 같다.
대각선 단위로 계산해볼까? 그게 맞는 것 같다.
가로 세로 첫번째줄은 전부 1로 두고
그리고 내 멋대로 그냥 0,0부터 인걸로 하자 그게 계산이 편하다
dp를 만드는데, puddles들은 전부 따로 표시를 해두자.

또 뭔가 이상한짓 했네.
dp[r][c]는 해당 지역까지 갈 수 있는 최단 경로 수라고 하자.
어떻게 구해
dp[r-1][c] + dp[r][c-1]이겠지

재귀로 하자 그냥
물웅덩이면 그냥 0
ㅠㅠ 효율적이지 못하다
반복문으로 해야하나
"""
# def recursion(r, c, dp):
#     max_r = len(dp)
#     max_c = len(dp[0])
#     if not (0 <= r < max_r and 0 <= c < max_c):
#         return 0
#     if dp[r][c]:
#         return dp[r][c] if dp[r][c] != 'p' else 0
#     dp[r][c] = recursion(r-1, c, dp) + recursion(r, c-1, dp)
#     return dp[r][c]

# def solution(m, n, puddles):
#     dp = [[0] * m for _ in range(n)]
#     dp[0][0] = 1
    
#     for pm, pn in puddles:
#         dp[pn-1][pm-1] = 'p'
    
#     return recursion(n-1, m-1, dp)


def solution(m, n, puddles):
    INF = 1000000007
    dp = [[0] * m for _ in range(n)]
    dp[0][0] = 1
    
    for pm, pn in puddles:
        dp[pn-1][pm-1] = 'p'
        
    for r in range(n):
        for c in range(m):
            if dp[r][c] == 'p':
                continue
            for nr, nc in ((r+1, c), (r, c+1)):
                if not (0 <= nr < n and 0 <= nc < m) or dp[nr][nc] == 'p':
                    continue
                dp[nr][nc] += dp[r][c]
                dp[nr][nc] %= INF
    
    return dp[n-1][m-1]