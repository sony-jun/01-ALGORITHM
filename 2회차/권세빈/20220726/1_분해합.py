# https://www.acmicpc.net/problem/2231

# 245의 분해합은 256(=245+2+4+5) 
# 따라서 245는 256의 생성자
#todo N의 가장 작은 생성자

n = int(input())
result = 0
for i in range(1, n+1):                 # 1 ~ n 까지의 숫자들
    a = sum(list(map(int, str(i))))     # str -> list하면 문자별로 리스트에 추가되는 것을 이용함
    if i + a == n:                      # 원래 값 + 각 자리수 합이 n일때
        result = i                      # 결과값에 할당
        break
print(result)




