def recursion(s, start, end, res):
    if start > end:
        return
    if start == end:
        res[start] = s[start]
        return print(''.join(res))
    
    min_a = s[end]
    min_i = end
    for i in range(start, end):
        a = s[i]
        if a >= min_a:
            continue
        min_a = a
        min_i = i
    res[min_i] = min_a
    print(''.join(res))
    recursion(s, min_i+1, end, res)
    recursion(s, start, min_i-1, res)

s = input()
res = [''] * len(s)
recursion(s, 0, len(s)-1, res)