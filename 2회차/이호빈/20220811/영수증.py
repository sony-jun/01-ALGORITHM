#총 금액를 받아준다
total = int(input())

#총 개수를 받아준다.
cnt = int(input())
#값을 누적할 변수
result = 0

#가격과 개수를 받아주고 
for i in range(cnt):
    price, cnt1 = map(int, input().split())
    #가격과 개수를 곱해주고 
    multiple = price * cnt1
    #결과값에 계산해준 값을 넣어준다.
    result += multiple

if total == result:
    print("Yes")
else:
    print("No")