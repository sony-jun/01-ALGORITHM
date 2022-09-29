# 카드 수량 받아서 초기 카드 배열을 리스트로 만들기, 좌측이 위쪽/우측이 아래쪽
card_list = [i for i in range(int(input()))]

# 카드가 1장만 남을 때까지 아래 작업 반복
while len(card_list) > 1:
    # 가장 먼저 있는 카드 출력 및 제거, end로 옆으로 출력
    print(card_list.pop(0), end=' ')
    # 제거했던 카드를 리스트 맨 뒤에 추가 
    card_list.append(card_list.pop(0))
# 반복문 종료 후 마지막 남은 요소 출력
print(card_list[0])
