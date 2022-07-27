# 어떤 정수들이 있습니다. 이 정수들의 절댓값을 차례대로 담은 정수 배열 absolutes와 
# 이 정수들의 부호를 차례대로 담은 불리언 배열 signs가 매개변수로 주어집니다. 
# 실제 정수들의 합을 구하여 return 하도록 solution 함수를 완성해주세요

def solution(absolutes, signs):
    number = []
    for i in range(len(signs)):
        if signs[i] == 1:
            number.append(absolutes[i])
        elif signs[i] == 0:
            number.append(-absolutes[i])   
    answer = sum(number) #number리스트의 합
    return answer #실제값들의 합
#1번 입출력
a = [4,7,12]
b = [True,False,True]
# #2번 입출력
# a = [1,2,3]	
# b = [False,False,True]

print(solution(a, b))