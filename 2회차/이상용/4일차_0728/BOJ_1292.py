# 쉽게 푸는 문제

# 동호는 내년에 초등학교를 입학한다. 
# 그래서 동호 어머니는 수학 선행 학습을 위해 쉽게 푸는 문제를 동호에게 주었다.
# 이 문제는 다음과 같다. 1을 한 번, 2를 두 번, 3을 세 번, 
# 이런 식으로 1 2 2 3 3 3 4 4 4 4 5 .. 이러한 수열을 만들고 
# 어느 일정한 구간을 주면 그 구간의 합을 구하는 것이다.
# 하지만 동호는 현재 더 어려운 문제를 푸느라 바쁘기에 우리가 동호를 도와주자.

# 1차 버전
# 두 수를 받는다.
x, y = map(int, input().split())

# 빈 리스트도 하나 만든다.
numbers = []

# 1은 1번, 2는 2번, 3은 3번 ... y는 y번으로 나가는 수열을 리스트로 만든다.
for i in range(1, y+1):
  for j in range(i):
    numbers.append(i)
  
# 수열에서 a부터 b번째 숫자 합까지 구한다
print(sum(numbers[x-1:y]))

##
# 코드 간소화 ver2
x, y = map(int, input().split())
numbers = [i for i in range(1, y+1) for j in range(i)]
print(sum(numbers[x-1:y]))
