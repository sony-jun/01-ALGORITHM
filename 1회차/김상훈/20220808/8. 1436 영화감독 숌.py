import sys
sys.stdin = open("8. 영화감독 숌.txt", "r")

# 666을 포함하는 숫자중에서 몇 번째 숫자?

N = int(input())
number = 666
cnt = 0
while True:
    if '666' in str(number):
        cnt += 1
    if cnt == N:
        print(number)
        break
    number += 1           
# number을 1씩 더해가는 while문을 만들어 666이 안에 들어있다면 cnt를 1 증가시키고,
# cnt가 n과 같다면 numbers을 출력해준다.
    
# 1. 666
# 2. 1666
# 3. 2666
# 4. 3666
# 5. 4666
# 6. 5666
# 7. 6660 6이 3번 나타나기 때문에 7번째 수는 6666이 아니라 6660
# 8. 6661 ...
