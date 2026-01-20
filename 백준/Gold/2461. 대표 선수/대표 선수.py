import sys
import heapq

input = sys.stdin.readline

N, M = map(int, input().split())
students = []
heap = []
idx = [0] * N

for i in range(N):
    arr = list(map(int, input().split()))
    arr.sort()
    students.append(arr)
    heapq.heappush(heap, (arr[0], i))

current_max = max(students[i][0] for i in range(N))
answer = current_max - heap[0][0]

while True:
    min_val, class_idx = heapq.heappop(heap)
    if idx[class_idx] + 1 == M:
        break
    idx[class_idx] += 1
    
    next_val = students[class_idx][idx[class_idx]]
    heapq.heappush(heap, (next_val, class_idx))
    
    if next_val > current_max:
        current_max = next_val
    
    answer = min(answer, current_max - heap[0][0])

print(answer)