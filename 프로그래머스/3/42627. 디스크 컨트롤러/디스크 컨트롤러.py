"""
우선순위 고려 사항 : 소요시간 -> 요청시간 -> 작업의 번호. 전부 작은 순으로.

작업 도중에 중단 안된다.
s가 요청 시점 <= 1000. i가 소요시간 <= 1000. 
소요시간을 turm ** 2으로 *해서 더하기. 요청시간은 * term 작업의 번호는 그냥

1. waiting이 차있으면?
1-1. 꺼내서 t를 끝나는 시간으로 넘긴다.
2. waiting이 안차있으면?
2-1. t를 아직 남은 애들 중 가장 작은 jobs로 넘긴다. -> 만약 아직 남은 애들이 없다면 break
3. request가 t보다 같거나 작은 애들을 waiting에 넣는다.
"""
from heapq import heappush, heappop
from collections import deque, namedtuple
Job = namedtuple('Job', ['duration', 'request', 'index'])

def solution(jobs):
    jobs = deque(sorted((Job(d, r, i) for i, (r, d) in enumerate(jobs)), key=lambda job: job.request))
    len_jobs = len(jobs)
    waiting = []
    t = 0
    total = 0
    while True:
        if waiting:
            job = heappop(waiting)
            t += job.duration
            total += t - job.request
        else:
            if jobs:
                t = jobs[0].request
            else:
                return total // len_jobs
        while jobs and jobs[0].request <= t:
            heappush(waiting, jobs.popleft())