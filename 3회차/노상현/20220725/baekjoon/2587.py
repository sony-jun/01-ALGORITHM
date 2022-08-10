# 10
# 40
# 30
# 60
# 30

# 다섯 개의 자연수가 주어질 때 이들의 평균과 중앙값을 구하는 프로그램을 작성하시오.

# 34
# 30



numbers = []    # 입력한 수들을 저장하는 리스트 변수 선언
for index in range(5):  #수 5개를 입력해야 하므로 5번 반복
    number = int(input())   #숫자를 입력하고 정수형으로 변환
    numbers.append(number)  #입력한 숫자를 numbers 리스트 변수에 넣어준다.
a = int(sum(numbers) /5 )   #numbers에 있는 숫자들을 모두 더하고 5로 나누어 평균을 구하는 변수를 선언
b = sorted(numbers)[2]  #numbers에 있는 숫자들을 오름차순으로 정렬하고 가운데 있는 숫자인 중앙값을 구하는 변수를 선언
print(a)    #평균값
print(b)    #중앙값
