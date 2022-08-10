# 숫자 순서대로 증가 시키며 666 포함 여부 문자열로 확인
n = int(input())

cnt = 0
number = 666
while True:
    if '666' in str(number):
        cnt += 1
        if cnt == n:
            break
    number += 1
print(number)