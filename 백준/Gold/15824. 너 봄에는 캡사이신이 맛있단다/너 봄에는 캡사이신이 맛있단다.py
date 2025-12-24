N = int(input())
scoville = sorted(map(int, input().split()))
maximum = 1000000007
pow = [1] * N
for i in range(1, N):
    pow[i] = (pow[i-1] << 1) % maximum
cnt = 0
for i in range(N):
    cnt = (cnt + scoville[i] * (pow[i] - pow[N-i-1])) % maximum
        
print(cnt)