# 어떤 정수들이 있습니다. 이 정수들의 절댓값을 차례대로 담은 정수 배열absolutes와 
# 이 정수들의 부호를 차례대로 담은 불리언 배열 signs가 매개변수로 주어집니다. 
# 실제 정수들의 합을 구하여 
# return 하도록 solution 함수를 완성해주세요.


# 정수와 불리언을 리스트로 2개의 리스트로 받는다.

# for문으로 정수리스트를 순회하며  

# 불리언 리스트의 값들을 True= 1 False = -1로 지정하여 곱한 후 result에 더 해서
 
#  for문이  끝나면 result값을  출력해준다.

num=list(map(int,input().split()))

bo=list(input().split())

result= 0

for n in range(len(num)):
    if bo[n] == 'True':
        bo[n]= 1
    elif bo[n] == 'False':
        bo[n]= -1
    result += num[n]*bo[n]

print(result)







# 제출용 
def solution(absolutes, signs):
    answer = 123456789
    
    result= 0

    for n in range(len(absolutes)):
        if signs[n] == True:
            signs[n]= 1
        elif signs[n] == False:
            signs[n]= -1
        result += absolutes[n]*signs[n]
    return result