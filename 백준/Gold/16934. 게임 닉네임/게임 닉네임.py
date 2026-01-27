import sys
input = lambda: sys.stdin.readline().rstrip()

class Node:
    def __init__(self):
        self.cnt = 0
        self.children = {}
        
root = Node()

for _ in range(int(input())):
    node = root
    alias = ''
    flag = True
    for a in input():
        if flag:
            alias += a
        if node.children.get(a) is not None:
            node = node.children.get(a)
            continue
        else:
            node.children[a] = Node()
            node = node.children[a]
            flag = False
        
    node.cnt += 1
    if node.cnt > 1:
        alias += str(node.cnt)
        
    print(alias)