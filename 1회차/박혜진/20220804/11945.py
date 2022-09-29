# 붕어빵의 개수 n
# 붕어빵의 모양을 나타내는 숫자열 m

n, m = map(int, input().split())

fish = []
# 붕어빵의 모양을 입력받으면 거꾸로 뒤집어 리스트에 저장
for _ in range(n) :
  fish.append(input()[::-1])

for i in fish :
  print(i)