N = int(input())                # 카드 개수 N

card = list(range(1, N+1))      # N개의 카드 리스트로 저장

while len(card) > 1:            # 카드 개수가 1개보다 많을 때까지
    print(card.pop(0), end=" ") # 첫번째 카드 출력한 후 제거
    card.append(card.pop(0))    # 첫번째 카드 리스트 마지막에 추가한 후 제거

print(*card)                    # 마지막 남은 카드까지 출력