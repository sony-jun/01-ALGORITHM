import sys

sys.stdin = open("64_수 정렬하기.txt")

N = int(input())
number_list = []
for tc in range(N):
    number = int(input())
   
    number_list.append(number)

number_list = sorted(number_list)

for tc in number_list: # 리스트의 숫자열 세로 나열하는법
    print(tc)

    