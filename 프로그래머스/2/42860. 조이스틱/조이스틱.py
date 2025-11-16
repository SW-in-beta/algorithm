"""
커서 이동 후 알파벳 변경
알파벳 변경은 쉬워보인다.
커서 이동 용 조이스틱 조작 횟수의 최솟값이 문제

name의 길이가 1이상 20이하. 최대 커서 이동 횟수는 name의 길이 맞나? ㅇㅋ
그럼 이동 횟수가 name의 길이보다 작은걸 찾아야 한다.
어떻게 찾나
뭔가 재귀의 느낌도 나고.

커서가 처음 0일때의 경우를 생각해보자.
0에 A가 아니면 그냥 바꾸면 된다.
그 경우를 제외하고는 오른쪽으로 가거나 왼쪽으로 가거나인데,

1. 오른쪽으로 간다고 생각하자.
그럼 거기서 또 바꾸고, 또 왼쪽으로 가냐 오른쪽으로 가냐 나뉘겠지
2. 왼쪽으로 간다고 생각해도 마찬가지.

그렇게 모든 경우를 다 구해야 하나? 20이니까 가능하긴 할듯

재귀라고 생각해보자.
현재의 위치에서 왼쪽 오른쪽으로 보내고 그 최솟값을 반환하면 되는데
종료 조건은 모든 알파벳이 동일하게 변했을 경우 -> 이걸 어떻게 판별할까
어차피 20이니까 별로 많진 않을 것 같으니 그냥 set으로 하자

recursion은 커서를 움직이는 횟수만 계산해보자. 알파벳은 그냥 일괄적으로 계산하는게 빠름

name으로 바꾸는건 어떻게? 복사해서 전달할까 아니면 백트래킹처럼?

recursion에서 계산해야하는 것
min(내가 왼쪽으로 이동하는 횟수 + 왼쪽으로 이동한 후의 이동횟수, 내가 오른쪽으로 이동하는 횟수 + 오른쪽으로 이동한 후의 이동 횟수)

new_name이 위로 오는게 맞다. 그래야 BAAAAA같은 경우를 해결할 수 있고, len(set(name))도 만약 'BBBB' 였다면 그냥 통과시켰겠지
"""

def recursion(name, index=0, cnt=0):
    new_name = name[:index] + 'A' + name[index+1:]
    if len(set(new_name)) == 1:#하...
        return cnt

    l_cnt = 0
    r_cnt = 0
    l_index = 0
    r_index = 0
    
    for i in range(1, len(name)):
        l = (index - i) % len(name)
        r = (index + i) % len(name)
        if new_name[l] != 'A' and l_cnt == 0:
            l_cnt = cnt + i
            l_index = l
        if new_name[r] != 'A' and r_cnt == 0:
            r_cnt = cnt + i
            r_index = r
        if l_cnt and r_cnt:
            break
    print(new_name, index, l_index, r_index, cnt)
    return min(recursion(new_name, l_index, l_cnt), recursion(new_name, r_index, r_cnt))

def solution(name):
    cnt = sum(min(ord(a) - ord('A'), ord('Z') - ord(a) + 1)for a in name)
    return cnt + recursion(name)