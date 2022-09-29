#문제: 분해합 값을 받아서 그 값의 생성자를 구하기

def nSum(n):
    nstr = str(n) #자릿수로 더하기 위해 문자열로 형변환
    s = n #분해합 구하기위해 각 자릿수를 더하기 전에 미리 입력값을 넣어 둠
    for i in range(len(nstr)):
        s += int(nstr[i]) # 자릿수를 더해 분해합만들기
    return s

def n_find(m):
    #생성자 찾기
    for i in range(m):
        #입력 받은 분해합과 범위 내 i를 분해합 구하는 함수 결과값이 일지하는 i 값 찾으면 i를 반환
        if m == nSum(i):
            return i
    return 0 #해당하는 값 없을시 0 반환


n = int(input())
print(n_find(n))

##다른 풀이

# N = int(input())

# for i in range(1,N+1):
#     resolve_sum = i
#     for j in range(len(str(i))):
#         resolve_sum += int(str(i)[j])
#     if resolve_sum == N:
#         print(i)
#         break
# else:
#     print(0)