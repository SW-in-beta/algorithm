"""
뭐야 이게
매번 gap이 하나인걸로만 갈 수 있나?
words들 사이의 관계를 정리를 해둬야겠다.
알파멧 소문자. 단어의 길이는 3이상 10이하. words는 50이하
변환할 수 없는 경우도 있다.
words들 사이에 간선을 정리해두자.
target이 words에 없으면 0

하나만 다른건 어떻게 찾지
길이가 3이상 10이하.
"""
from collections import deque
INF = float('inf')

def get_diff_cnt(word1, word2):
    diff = sum(int(w1 != w2) for w1, w2 in zip(word1, word2))
    return diff

def solution(begin, target, words):
    if target not in words:
        return 0
    
    words = [begin] + words
    graph = [[] for _ in range(len(words))]
    cnts = [INF] * len(words)
    
    for i in range(len(words)):
        for j in range(i, len(words)):
            word1, word2 = words[i], words[j]
            if get_diff_cnt(word1, word2) == 1:
                graph[i].append(j)
                graph[j].append(i)
                
    q = deque([(0, 0)])
    while q:
        i, cnt = q.popleft()
        word = words[i]
        if word == target:
            return cnt
        if cnts[i] <= cnt:
            continue
        cnts[i] = cnt
        cnt += 1
        
        for j in graph[i]:
            if cnts[j] > cnt:
                q.append((j, cnt))
        
    return 0