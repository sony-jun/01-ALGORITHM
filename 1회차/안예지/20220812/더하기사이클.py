# 1110.
"""
"""
"""======================google======================"""

n = input()
num = n
cnt = 0

while 1:
    if len(num) == 1:
        num = "0" + num
    plus = int(num[0]) + int(num[1])
    num = num[-1] + str(plus)[-1]
    cnt += 1
    
    if num == n:
        print(cnt)
        break

     
"""======================google======================"""
"""
N = int(input())    # 입력값
new_num = N
cnt = 0

while True:
    
    ten = new_num // 10 # 입력값을 10으로 나눈 몫 ( 십의 자리 )
    one = new_num % 10 # 입력값을 10으로 나눈 나머지( 일의 자리 )
    sum_num = ten + one
    new_ten = one * 10  # 새로운 숫자의 10의 자리값 획득
    new_one = sum_num % 10 # 새로운 숫자의 1의 자리값 획득
    new_num = new_ten + new_one # 새로운 숫자
    cnt += 1
    
    if N == new_num:
        print(cnt)
        break
"""