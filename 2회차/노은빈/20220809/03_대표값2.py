import sys
input = sys.stdin.readline

num = []  #숫자가 들어갈 빈 리스트

for _ in range(5): #들어갈 숫자의 개수만큼 반복
    n = int(input())
    num.append(n) #리스트에 input 넣어주기
    num.sort()

print(int(sum(num)/len(num)))  #평균 = 합/리스트 길이
print(num[2])  #중앙값 인덱스 위치