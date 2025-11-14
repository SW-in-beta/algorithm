"""
일단 sort 한 번 하자
그리고 가장 끝에 하나 설치하고
다음꺼 하나씩 꺼내면서 가장 끝에 걸치면 패스 아니면 또 끝에 설치

이 코드의 문제점 [-20, -10] [-5, -3] 이 경우 두 개를 설치한다.
어떻게 방지할 수 있지?
최소한의 커버리지를 선택한다?
"""
def solution(routes):
    cnt = 0
    last = -30001
    for s, e in sorted(routes):
        if s <= last <= e:
            continue
        elif e < last:
            last = e
            continue
        cnt += 1
        last = e
    return cnt