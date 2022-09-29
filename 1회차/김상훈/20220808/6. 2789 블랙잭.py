import sys
sys.stdin = open("6. 블랙잭.txt", "r")

input = sys.stdin.readline
max_cards = 0
N, M = map(int,input().split())
cards = list(map(int,input().split()))
for i in range(N-2): # 2장은 어떻게 뽑혀야하고,나머지 3개중에 하나를 뽑는 것이기 때문에 끝까지 돌 필요 없음.
    for j in range(i+1,N-1): # 첫 번쨰 for문 다음꺼부터 시작. 본인말고 다른 하나만 선택하면 됨.
        for k in range(j+1,N): # 두번쨰 for 다음꺼부터 시작 
            total_cards = cards[i] + cards[j] + cards[k]
            if max_cards < total_cards <= M :
                max_cards = total_cards
                if max_cards == M:
                    break
print(max_cards)
                
            
