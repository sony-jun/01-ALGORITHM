
# from re import L


# num = input()

# load = list(map(int, input().split()))
# uphill = []
# cnt = 0
# for i in range(len(load)) :
#     if i == 0 :
#         uphill.append(load[i])
    
#     elif i == len(load)-1 :
#         if load[i] > load[i-1] :
#             uphill.append(load[i])
#     elif load[i] >= load[i+1] and load[i] >= load[i-1] :    #오르막길 꼭짓점
#         uphill.append(load[i])
#     elif load[i] < load[i-1] :                 # 오르막길 시작
#         uphill.append(load[i])
# uphillsize = []
# print(uphill)
# for j in range(1, len(uphill)) :
#     uphillsize.append(uphill[j] - uphill[j-1])

# print(max(uphillsize))


import sys                        ## 수운이 풀이
sys.stdin = open('bj2846.txt', 'r')     ## a, b를 오르막길의 시작과 끝의 인덱스로 활용한다. 
num = input()
load = list(map(int, input().split()))


result = 0           ## 결과값

a = 0           ## 오르막길 시작
b = 0           ## 오르막길 끝
# num = 5
while b  < int(num) -1:         ## 뒤에 if 문의 [b+1] 이 리스트의 끝에 오도록 하기 위한 조건문
    if load[b] < load[b+1]:     ## 오르막길이 계속되면 b의 위치를 바꿔준다.
        b += 1

    else:
        if load[b] - load[a] > result:  ## 오르막길이 끝났으면 해당 오르막길의 크기를 계산하고,
            result = load[b] - load[a]  ## result에 대입(이 전 오르막길보다 큰 경우만)
        a, b = b+1, b+1          ## 다음 오르막길 시작. 

if load[b] - load[a] > result:  # 앞의 while문은 마지막 오르막길 크기를 비교하지 않기 때문에 (else문이 안돔)
    result = load[b] - load[a]  ## 마지막으로 한번 더 비교해준다. 

print(result)


