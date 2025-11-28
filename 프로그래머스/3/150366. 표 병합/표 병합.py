"""
크기는 50 * 50 고정. 모든 셀은 비어있다.
병합은 Redirect 느낌. 부모를 설정해주면 되겠다. 유니온 파인드?
병합을 해제하면 값은 r, c만 가지고 나머지 셀은 전부 비어있는 상태로 돌아간다
병합된 셀을 또 병합하면 어떻게 되려나-> 부모가 되는 녀석의 값을 가지는거지 뭐
결국 부모를 저장해두고, UPDATE는 부모의 값만 업데이트 해주면 되는거 같은데
UPDATE는 일단 값을 찾아서 부모의 값을 업데이트
MERGE는 부모를 변경
UNMERGE는 값을 찾아 해당 위치에 병합 + 같은 부모를 가진 아이들의 부모를 되돌리고 전부 비도록
"""

size = 50 * 50
values = [None] * size
parents = [i for i in range(size)]

def find(i):
    if parents[i] != i:
        parents[i] = find(parents[i])
    return parents[i]

def rc_2_idx(r, c):
    return (r - 1) * 50 + c - 1

def update(*args):
    if len(args) == 3:
        idx = rc_2_idx(*map(int, args[:2]))
        return update_by_idx(idx, args[2])
    else:
        return update_by_value(*args)

def update_by_idx(idx, value):
    p_idx = find(idx)
    values[p_idx] = value
    
def update_by_value(target, value):
    for i in range(size):
        p_idx = find(i)
        if values[p_idx] != target:
            continue
        values[p_idx] = value

def merge(r1, c1, r2, c2):
    idx1 = rc_2_idx(int(r1), int(c1))
    idx2 = rc_2_idx(int(r2), int(c2))
    if idx1 == idx2:              
        return
    p_idx1 = find(idx1)
    p_idx2 = find(idx2)
    if p_idx1 == p_idx2:
        return
    value = values[p_idx1] if values[p_idx1] != None else values[p_idx2]
    values[p_idx1] = value
    parents[p_idx2] = p_idx1
    for i in range(size):
        find(i)
    
def unmerge(r, c):
    idx = rc_2_idx(int(r), int(c))
    p_idx = find(idx)
    value = values[p_idx]
    for i in range(size):
        if find(i) != p_idx:
            continue
        parents[i] = i
        values[i] = None
    values[idx] = value
    
def print_value(r, c):
    idx = rc_2_idx(int(r), int(c))
    p_idx = find(idx)
    return values[p_idx] if values[p_idx] != None else "EMPTY"
    
command_dict = {"UPDATE": update, "MERGE": merge, "UNMERGE": unmerge, "PRINT": print_value}

def solution(commands):
    answer = []
    for command in commands:
        c, *args = command.split(' ')
        res = command_dict[c](*args)
        if c == "PRINT":
            answer.append(res)
    return answer