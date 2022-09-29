# input으로 주어진 집합 a, b를 쪼개고 int 형변환 한다.
a, b = map(int, input().split())
# 대칭 차집합
num1 = set(map(int, input().split()))
num2 = set(map(int, input().split()))
print(len(num1-num2)+len(num2-num1))