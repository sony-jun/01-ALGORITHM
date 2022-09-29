
import sys
sys.stdin = open('자료구조는정말최고야.txt','r')

# sorted로 풀어보자
# 4 2
# 2
# 3 1
# 2
# 4 2

# 5 2
# 3
# 3 5 1
# 2
# 4 2

N, M = map(int,input().split()) #N:전체책수. M:묶음수

MK = [] #각묶음의 책개수
list_ = [] #각묶음의 책번호, 인덱스가 자리
for m in range(M):
    MK.append(int(input()))
    list_.append(list(map(int,input().split())))

print(list_,MK,'초기값')
for n in range(1,N+1): #책의 갯수만큼 반복 1234 / n책의 번호
    for m in range(M): #묶음 갯수 반복 123 / 묶음을 순환
        if MK[m] > 0 and list_[m][MK[m]-1] == n : #책의갯수판별0 , 리스트마지막변수가 == n인가
            MK[m] -= 1 #묶음에 있는 권수를 줄인다.
            list_[m].pop() #묶음에 있는 번호는 뺸다
            print(list_,MK) #list_와MK변화

if sum(MK) == 0 :
    print('Yes')
else:
    print('No')