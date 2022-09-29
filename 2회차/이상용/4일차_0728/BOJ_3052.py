# 나머지

# 두 자연수 A와 B가 있을 때, A%B는 A를 B로 나눈 나머지 이다. 
# 예를 들어, 7, 14, 27, 38을 3으로 나눈 나머지는 1, 2, 0, 2이다. 
# 수 10개를 입력받은 뒤, 이를 42로 나눈 나머지를 구한다. 
# 그 다음 서로 다른 값이 몇 개 있는지 출력하는 프로그램을 작성하시오.

# 초기모델 ver1
# 빈 리스트 만들기
numbers = []

# 수 10개를 입력받기 + 42로 나눈 나머지를 리스트에 넣기
for i in range(10):
  N = numbers.append(int(input()) % 42)

# 중복값 제거 후 개수 확인
result = set(numbers)
print(len(result))

##
# 코드 간소화 ver2
numbers = set([int(input()) % 42 for i in range(10)])
print(len(numbers))