"""
모든 경우의 수를 구하기에는 자리수가 너무 많다.
지운다기보다 뽑는다는 생각으로 가보자.
뽑아야 하는 수 : len(number) - k개.
어떤 기준으로 뽑아야 할까.

큰 수 기준으로 보자.
큰 수 앞에 숫자들을 모두 버려도 뽑아야 하는 수 이상이 남는다면? 뽑는게 맞다.
그리고는 그 다음부터 보는거. 
근데 만약 큰 수 앞에 숫자들을 모두 버리면 뽑아야 하는 수 이상이 안남는다?
그럼 앞에 숫자는 버리지 않는 선에서, 그 큰 수는 포함해야 하나 버려야 하나?
일단 당연히 포함은 한다.
근데 이제 뒤에 있는 친구들은 다 남기고, 제거해야할 대상들을 앞에서 뽑아야 이득

여기까지 정리
1. 큰 수 기준으로 정렬 후 하나씩 보기
1.1 해당 큰수 기준으로 앞에 모두 버린다고 가정하자.
다 버려도 남은 개수가 뽑아야 하는 수보다 같거나 크다? 그럼 다 버리고, 뽑아야 하는 수 -1. 그리고 그 뒷 친구들 대상으로만 진행
다 버리면 남은 개수가 뽑아야 하는 수보다 작다? 그럼 뒤에 있는 애들은 다 뽑고, 그 앞 친구들 대상으로만 진행

검사 대상인 min_idx와 max_idx를 조절하면서 가자.
그럼 종료 조건은 어떻게 되나.
뽑아야 하는 수가 0이 되었을때는 당연.
그리고 대상으로 진행해야할 친구들이 뽑아야 하는 수라면 다 포함시키기.

그러면 뽑힌 친구들을 어떻게 관리해야할지
중간에서도 뽑힐 수 있으니까. 그냥 다 뽑아놓고 또 정렬하자 귀찮다. 시간초과 나면 그때 생각해보자.
"""
from collections import deque
def solution(number, k):
    target_cnt = len(number) - k
    q = deque(sorted([(n, -i) for i, n in enumerate(number)], reverse=True))
    min_idx = 0
    max_idx = len(number) - 1
    answer = []
    
    while target_cnt:
        n, i = q.popleft()
        i = -i
        if i < min_idx or i > max_idx:
            continue
        remained = max_idx - i + 1
        if remained >= target_cnt:
            target_cnt -= 1
            answer.append(i)
            min_idx = i + 1
        else:
            target_cnt -= remained
            answer.extend([idx for idx in range(i, max_idx + 1)])
            max_idx = i - 1
        if max_idx - min_idx + 1 == target_cnt:
            answer.extend([idx for idx in range(min_idx, max_idx + 1)])
            break
        
    return ''.join(number[i] for i in sorted(answer))