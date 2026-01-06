A, B = map(lambda x: bin(int(x))[2:], input().split())

def one_cnt(num, pre=0):
    exp = len(num) - 1
    if exp == 0:
        return 1 + pre
    cur_sum = exp * (2 ** (exp - 1)) + 1
    cur_sum += pre * (2 ** exp)
    i = 1
    while i < len(num) and num[i] == '0':
        i += 1
    if i < len(num):
        cur_sum += one_cnt(num[i:], pre + 1)
    return cur_sum
cnt_A = sum(int(i) for i in A)
print(one_cnt(B) - one_cnt(A) + cnt_A)