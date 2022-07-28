#뒤집힌 더셈
a, b = map(str, input().split())

# 각각 리버스하고 숫자형으로
rev_a = int(a[::-1])
rev_b = int(b[::-1])
# 문제에 나오는 식을 사용한거
rev_ab = str(rev_a + rev_b)[::-1]
print(int(rev_ab)) 
#마지막에 int를 안하면 01 이런식으로 나와서 int사용

