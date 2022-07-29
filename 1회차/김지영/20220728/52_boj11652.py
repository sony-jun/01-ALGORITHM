N = int(input())
card = {}
for _ in range(N):
    num = int(input())
    if num not in card:
        card[num] = 1
    else : card[num] += 1
# print(card)
maxvalue = max(card.values())   # O(N)
maxkey = [k for k,v in card.items() if maxvalue==v] # O(N)

# for문 돌릴때마다 max함수가 돌아가서 시간이 비싸요!!! O(N^2)
# maxkey = [k for k,v in card.items() if max(card.values())==v] # 시간초과
print(min(maxkey))