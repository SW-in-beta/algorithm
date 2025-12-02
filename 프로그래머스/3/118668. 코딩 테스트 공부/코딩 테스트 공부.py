def solution(alp, cop, problems):
    # 1. 필요한 최대 알고력 / 코딩력 계산
    max_alp_req = max(p[0] for p in problems)
    max_cop_req = max(p[1] for p in problems)

    # 이미 충분히 크면 더 키울 필요 없음 (범위 줄이기)
    alp = min(alp, max_alp_req)
    cop = min(cop, max_cop_req)

    INF = 10**9
    # dp[a][c] : 알고력 a, 코딩력 c에 도달하는 최소 시간
    dp = [[INF] * (max_cop_req + 1) for _ in range(max_alp_req + 1)]
    dp[alp][cop] = 0

    for a in range(alp, max_alp_req + 1):
        for c in range(cop, max_cop_req + 1):
            # 현재 상태까지 도달하는 게 이미 말도 안 되게 크면 스킵
            if dp[a][c] == INF:
                continue

            # 1) 알고력 공부 (a+1, c)
            if a + 1 <= max_alp_req:
                dp[a + 1][c] = min(dp[a + 1][c], dp[a][c] + 1)

            # 2) 코딩력 공부 (a, c+1)
            if c + 1 <= max_cop_req:
                dp[a][c + 1] = min(dp[a][c + 1], dp[a][c] + 1)

            # 3) 문제 풀기
            for req_a, req_c, rwd_a, rwd_c, cost in problems:
                if a >= req_a and c >= req_c:
                    na = min(max_alp_req, a + rwd_a)
                    nc = min(max_cop_req, c + rwd_c)
                    dp[na][nc] = min(dp[na][nc], dp[a][c] + cost)

    return dp[max_alp_req][max_cop_req]