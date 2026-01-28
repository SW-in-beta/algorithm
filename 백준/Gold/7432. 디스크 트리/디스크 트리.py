import sys
input = lambda: sys.stdin.readline().rstrip()

class Node:
    def __init__(self, layer=0):
        self.layer = layer
        self.children = {}
        
    def get_children(self):
        for key, value in sorted(self.children.items()):
            yield ' ' * self.layer + key, value

def print_node(node):
    for value, child in node.get_children():
        print(value)
        print_node(child)
            
root = Node()
N = int(input())

for _ in range(N):
    node = root
    for directory in input().split('\\'):
        cur = node.children.get(directory)
        if cur is None:
            cur = Node(node.layer + 1)
            node.children[directory] = cur
        node = cur

print_node(root)