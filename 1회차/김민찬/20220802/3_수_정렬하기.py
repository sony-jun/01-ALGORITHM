import sys

sys.stdin = open("3_수_정렬하기.txt")

N = int(input())
num_list = [] # 숫자들의 리스트를 만든다.

for i in range(N): # N 만큼 반복
    num_list.append(int(input())) # num_list에 항목들을 추가
num_list1 = sorted(num_list) # sorted로 정렬(오름차순)

for i in range(len(num_list)):
    print(num_list1[i]) # 요소들을 하나씩 출력