import sys
sys.stdin = open("2750.txt")

N = int(input())
number = [] # 리스트 생성
for i in range(N):
    number.append(int(input())) # 입력 받은 수를 number 리스트에 추가

number.sort() # sort로 정렬 (오름차순이 기본값)
for i in range(len(number)): # number 리스트 길이만큼 i순휘
    print(number[i]) # number 리스트를 모두 출력
