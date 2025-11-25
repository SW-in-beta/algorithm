"""
카드 1~n, 동전 coin개.
내가 가진 카드는 항상 짝수개. 카드는 동전써서 가지거나 그냥 버리거나

coin의 길이는 n. 
card 길이는 1000 미만

가지느냐 안가지느냐를 계산해야한다.

1. 우선 현재 가지고 있는 패에서 안가지고 갈 수 있는 최대 턴을 찾는다.
2. 그 최대 턴 안에서 추가된 카드 중에, 내가 어떤 것들을 가져야 최고로 더 갈 수 있는지 볼 수 있다.

그 안에서 또 뽑았을 때 최대로 더 갈 수 있는 턴을 구한다. 그 다음에 또 반복 반복하면 될 것 같은데?

그렇게 했을 때 두개를 뽑아야 갈 수도 있다..
한장을 뽑아서 갈 수 있으면 무조건 뽑기
한장을 못뽑으면 후보

그럼 관리해야할 것.
내가 필요로 하는 패(set)
후보로 필요로 하는 패(set)
내가 필요로 하는 패가 있으면 코인 1개 쓰고 가지면 됨
없으면 후보로 필요로 하는 패 중에서 coin 2개 쓰고 하면 된다.
"""
def pick_card(i, j, cards, coin, need, candidate):
    picked = set()
    for card in cards[i:j]:
        pocket = picked if card in need else candidate
        pocket.add(card)
            
    if picked:
        need -= picked
        turn = min(coin, len(picked))
        return turn, coin - turn
    
    if coin < 2:
        return 0, coin
    
    for card in candidate:
        next_card = len(cards) + 1 - card
        if next_card in candidate:
            candidate.remove(card)
            candidate.remove(next_card)
            return 1, coin - 2
    
    return 0, coin
            

def solution(coin, cards):
    n = len(cards)
    need = set(n + 1 - card for card in cards[:n // 3])
    candidate = set()
    
    turn = 1
    i = n // 3
    for card in cards[:n // 3]:
        if card in need:
            need.remove(card)
            need.remove(n + 1 - card)
            turn += 1        
    j = i + turn * 2
    
    while True:
        added_turn, coin = pick_card(i, j, cards, coin, need, candidate)
        if added_turn == 0 or coin == 0:
            break
        i = j
        j = i + added_turn * 2
        turn += added_turn
        
    return min(turn + added_turn, n // 3 + 1)