from re import A
import sys

sys.stdin = open("input5576.txt")

#맨 처음 input값.
#w,k = list(map(int,input().split()))

w_score = [] #빈 리스트 w,k 정의해주고.
k_score = []

for i in range(10):
    w_score.append(int(input()))
for j in range(10):
    k_score.append(int(input()))

w_score.sort(reverse=True)#내림차순정렬(원본을 역정렬하고 수정합니다)
#print(w_score)해보면 [23, 23, 20, 15, 15, 14, 13, 9, 7, 6]
k_score.sort(reverse=True)
#print(k_score) 해보면 [25, 19, 17, 17, 16, 13, 12, 11, 9, 5]

print(sum(w_score[:3]), sum(k_score[:3]))
###===============================
# 단순히 생각 할 필요가 있다. input값이랑 변수값부터 좌라락나열하고 시작하지않기
# sort(reverse=True) vs reverse()
# 순회 하면서 w,k_score에 값 넣어주고
# sort( ), reverse( ) 모두 리스트 메소드입니다.
# sort( )는 기준에 따라 오름차순 또는 내림차순 정렬을 하는 것이고, 
# reverse( )는 단순히 리스트의 순서를 뒤집는 것입니다.
