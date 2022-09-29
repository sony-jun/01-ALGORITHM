# 입력 개수 N과 M 받기
N, M = map(int, input().split())

# M 만큼 반복해서 교과서 수, 각 교과서 번호 받기
for _ in range(M):
    book_num = int(input())
    book_list = list(map(int, input().split()))
    
    # 교과서 번호들 내림차순인지 확인
    if book_list != sorted(book_list, reverse = True):
         result = 'No'
         break
    else:
        result = 'Yes'

print(result)
