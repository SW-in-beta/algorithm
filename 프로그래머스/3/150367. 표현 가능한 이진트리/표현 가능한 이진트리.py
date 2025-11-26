"""
나는 이진트리를 수로 표현하는 것을 좋아한다.
1. 포화 이진트리로 만들고, -> 이게 핵심일 것 같다.
2. 가장 왼쪽부터 오른쪽 노드까지 순서대로. -> 중위순환이다.
3. 더미면 0추가, 아니면 1추가. 저장된 이진수를 십진수로 변환

예시를 보자. 42는 이진수로 101010 -> 길이를 포화 이진트리로 맞춰야 하니까 0101010 -> 만들 수 있다.
5는? 101 -> 루트가 없는 상태다. X
자신의 부모가 없는데 노드가 있으면 안되는 거.
중위 순회에서 부모를 어떻게 찾아..
중위 순화를 전위 순회로 변경해야하나?
이거 재귀로 될 것 같다.
제일 중앙이 0이면? 양쪽에 1이 있으면 실패. 전부 0이면 성공
만약 제일 중앙이 1이면? 양쪽으로 판단을 맡겨야지. 양쪽 다 성공하면 성공이고 양쪽중에 하나라도 실패하면 실패
"""
import sys

def pad(binary):
    n = 1
    while 2 ** n - 1 < len(binary):
        n += 1
    return binary.zfill(2 ** n - 1)

def num_2_tree(num):
    return pad(bin(num)[2:])

def is_binary_tree(tree, i=None, j=None):
    i = 0 if i == None else i
    j = len(tree)-1 if j == None else j
    center = (i + j) // 2
    if i == j:
        return True
    if tree[center] == '0':
        return int(tree[i:center]) + int(tree[center+1:j+1]) == 0
    return is_binary_tree(tree, i, center-1) and is_binary_tree(tree, center+1, j)

def solution(numbers):
    return [1 if is_binary_tree(num_2_tree(num)) else 0 for num in numbers]