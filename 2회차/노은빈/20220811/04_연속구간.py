import sys
sys.stdin = open("연속구간.txt")

result = []
for i in range(3): #입력받는 숫자 한 줄 개수만큼
    num = input()
    cnt = 1 #연속하는 숫자의 개수
    list_ = [] #cnt 리스트
# print(num)
    for j in range(1, 8):
        if num[j] == num[j - 1]: #앞과 뒤과 같으면 
            cnt += 1
        else :
            list_.append(cnt)
            cnt = 1
            #리스트는 구글링함
    list_.append(cnt) #리스트에 cnt 값 추가
    result.append(max(list_)) #가장 큰 값
print(*result, sep='\n') #한 줄씩 띄어서 출력 





