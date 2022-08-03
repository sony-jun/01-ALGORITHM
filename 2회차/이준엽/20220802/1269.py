a, b = map(int,input().split())
numbers_a = list(map(int,input().split()))
numbers_b = list(map(int,input().split()))
result = (set(numbers_a)-set(numbers_b))|(set(numbers_b)-set(numbers_a))
print(len(result))

# set()함수를 통해 집합의 차집합 교집합 합집합을 구할때는
# 합집합 = '|' 기호
# 교집합 = '&' 기호
# 차집합 = '-' 기호
# 를 이용한다.