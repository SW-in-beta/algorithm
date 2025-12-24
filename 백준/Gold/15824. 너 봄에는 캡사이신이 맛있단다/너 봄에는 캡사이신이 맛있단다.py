N = int(input())
scoville = sorted(map(int, input().split()))

cnt = 0
add = 1
sub = 2 ** (N - 1)
for i in range(N):
    cnt += (add - 1) * scoville[i] - (sub - 1) * scoville[i]
    add <<= 1
    sub >>= 1
    cnt %= 1000000007
        
print(cnt)