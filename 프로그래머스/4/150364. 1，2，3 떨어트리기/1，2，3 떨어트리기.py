"""
번호가 작은 노드를 가리키는 간선을 초기 길로
숫자가 리프 노드에 도착하면, 길을 순환시킨다.
근데 떨어뜨리면 어떻게 되는거야.
이거 길순환은 재귀로 해야겠다.

어려울 것 같은 점 : 모든 노드에 얼만큼의 횟수가 돌아가냐를 알아야 한다.
이거 사전에 쌓이는 순서를 알 수 있지 않을까?

edge 길이 100까지.
뭔가 재귀의 느낌인데.
리프 순환 순서가 맞아떨어지진 않는다.
위에서 분배해주는 만큼 나눠가져야 하는데
각 리프에서 나한테 순서가 얼마나 자주 돌아오는지 확인해볼까? -> ㅇㅋ
내 부모들의 간선 수의 곱마다 한 번씩 돌아온다. 그리고 초기 순서도 알 수 있다. -> 어떻게?
그럼 초기 순서대로 힙에 넣되, 빼고 나서는 돌아오는 순서를 더해 넣으면 된다.

목표는 target과 같은 값을 가리키게. 가장 적은 숫자를 사용하는게 우선 + 그 다음에 사전 순으로 가장 빠른 경우
그럼 target에 가까워질때까지는 3을 계속 더하기. target에 도달했으면 쪼개기.

초기 순서를 어떻게 알 수 있을까.
리프의 부모들만 놓고 생각하자.
자기 부모가 몇명을 두고 있는지 보고, 반복해서 시퀀스를 만든다.
근데 얼마마다 한 번씩 돌아오는지 아는데, 그걸로 구할 수는 없나? -> 없을 것 같다.

구할 수 있다. 부모들을 타고 타고 가면서 자신이 몇번째 인지 계산하면?
이거 생각 잘해보자.
내 부모의 차례가 얼마에 한 번씩 돌아오는지
위치 * 내가 몇번짼지. 결국 똑같다.

이 트리 내에서 내가 차지하는 위치(0부터) * 루트의 형제노드 수 + 내 루트의 위치(1부터)
이걸 재귀로 좀 정리해보자.
위에서부터 내려와야하나? 아래에서부터 올라가야하나?

"""
from collections import deque

"""
역할을 명확히 정하자.
root : 현재의 root
turn : 현재의 루트 아래에서 내가 갖는 위치
구하고자 하는 것 -> root를 한 단계 더 위로 올렸을 때 내가 갖는 위치
"""
from heapq import heappush, heappop, heapify
from collections import deque

def get_first_turn(leaf, tree, parents):
    if len(tree[leaf]) > 0:
        return 0
    parent = parents[leaf]
    childs = tree[parent]
    total_turn = childs.index(leaf) + 1
    
    while parent != 1:
        leaf = parent
        parent = parents[leaf]
        childs = tree[parent]
        turn = childs.index(leaf) + 1
        total_turn = (total_turn - 1) * len(childs) + turn
    
    return total_turn

def get_cycle(node, tree, parents):
    if len(tree[node]) > 0:
        return 0
    
    cycle = 1
    while node != 1:
        node = parents[node]
        cycle *= len(tree[node])
    return cycle

def solution(edges, target):
    target = [0] + target
    tree = [[] for _ in range(len(target))]
    parents = [i for i in range(len(target))]
    for p, c in edges:
        tree[p].append(c)
        parents[c] = p
    for childs in tree:
        childs.sort()
    cycle = [0]
    first_turn = [0]
    for n in range(1, len(target)):
        cycle.append(get_cycle(n, tree, parents))
        first_turn.append(get_first_turn(n, tree, parents))
    
    h = [(t, n) for n, t in enumerate(first_turn) if t > 0]
    heapify(h)
    result = [0] * (len(target))
    
    """
    이제 어떻게 넣을지 생각해보자.
    target보다 작으면 min(3, target-result)
    target과 같으면 쪼개기.
    2가 있다면 2를 1과 1로
    2가 없다면 3을 1과 2로
    3도 없다면 더이상 -1이 답
    
    저걸 그러니까 어떻게 꺼낼거냐고.
    2는 뒤로 넣고 1은 앞으로 넣고? ㅇㅋ
    마지막이 1이면 패스
    """
    accumulates = [deque([]) for _ in range(len(target) + 1)]
    
    while result != target:
        t, n = heappop(h)
        if result[n] < target[n]:
            num = min(3, target[n] - result[n])
            result[n] += num
            if num == 1:
                accumulates[n].appendleft(num)
            else:
                accumulates[n].append(num)
        else:
            if accumulates[n][-1] == 1:
                return [-1]
            num = accumulates[n].pop()
            accumulates[n].appendleft(1)
            if num == 2:
                accumulates[n].appendleft(1)
            else:
                accumulates[n].append(2)
        heappush(h, (t + cycle[n], n))
        
    h = [(t, n) for n, t in enumerate(first_turn) if t > 0]
    heapify(h)
    
    result = []
    while True:
        t, n = heappop(h)
        if len(accumulates[n]) == 0:
            break
        
        if accumulates[n][0] == 1:
            v = accumulates[n].popleft()
        else:
            v = accumulates[n].pop()
    
        result.append(v)
        heappush(h, (t + cycle[n], n))
        
    return result