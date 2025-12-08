import sys
from heapq import heappush, heappop
input = lambda: sys.stdin.readline().rstrip()

days_per_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
month_to_day = [0] * 13
for i in range(1, 13):
    month_to_day[i] = month_to_day[i-1] + days_per_month[i-1]

def to_day(month, date):
    return month_to_day[int(month)] + int(date)

start_min_h = []
end_max_h = []
pivot_start_day = to_day(3, 1)
pivot_end_day = to_day(11, 30)

N = int(input())
for _ in range(N):
    start_month, start_date, end_month, end_date = input().split()
    start_day = to_day(start_month, start_date)
    end_day = to_day(end_month, end_date)

    heappush(start_min_h, (start_day, end_day))
    if start_day <= pivot_start_day:
        heappush(end_max_h, - end_day)

cnt = 0
while end_max_h:
    cur_end_day = - heappop(end_max_h)
    if cur_end_day <= pivot_start_day:
        break
    cnt += 1
    pivot_start_day = cur_end_day

    if pivot_start_day > pivot_end_day:
        print(cnt)
        exit()

    while start_min_h and start_min_h[0][0] <= pivot_start_day:
        heappush(end_max_h, - heappop(start_min_h)[1])

print(0)