# 주어진 N개의 수 받음
N = int(input())
# 빈 리스트 만듬
num_list = []
# N의 range를 처음부터 끝까지 돌아서 index 꺼냄
for i in range(N):
    # int로 형변환 한 N을 num_list에 추가
    num_list.append(int(input()))
# num_list sort해서 정렬
num_list.sort()
# num_list에 있는 j를 처음부터 끝까지 돌아서 꺼냄
for j in num_list:
    # j 출력
    print(j)


