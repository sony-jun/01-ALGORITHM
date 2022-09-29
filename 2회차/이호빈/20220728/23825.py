n, m = input().split() # 입력값을 받고

s = 'S' * int(n) # S의 개수를 n을 곱한만큼 늘린다
a = 'A' * int(m) # A의 개수를 m을 곱한만큼 늘린다.

new_string = "" # 문자열을 담을 변수
for s1, a1 in zip(s, a): #zip을 활용해서 s,a 두 변수를 돌아주고
    new_string += s1 + a1 # 값들을 차례대로 더해주고
print(new_string.count("SASA")) #count함수를 사용해서 출력

# 2. 다른 방법
result = ''.join(map(''.join, zip(s, a)))
print(result.count("SASA"))