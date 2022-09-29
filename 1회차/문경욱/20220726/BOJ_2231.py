N = input()
first_N = int(N)
gene_num = 0

while int(N) != 0:
    N = str(int(N)-1)
    # 계산 반복을 위해 0으로 초기화
    total_num = 0

    # 각 자릿수의 합
    for number in N:
        total_num += int(number)
    
    # 생성자가 있는지 없는지 검사 ex) 215 + 2 + 1 + 5 =? 216
    if first_N == int(N) + total_num :
        gene_num = int(N)
    
print(gene_num)


'''
N = int(input())

# 1부터 N 사이의 보든 수의 분해합을 탐색
for number in range(1,N):
    print(number)
    # 분해합 저장 변수
    split_sum = 0

    # 각 자리수의 합
    for digit in str(number):
        split_sum = split_sum + int(digit)

    # 각 자리수의 합 + 수의 합 => 분해합
    split_sum = split_sum + number

    # 구한 분해합과 입력 N이 같으면
    # number는 N의 생성자
    if N == splist_sum:
        print(number)
        break # 가장 작은 생성자를 탐색

# for-else
# break를 만나지 않으면 else 실행
# 생성자가 없을 때 0을 출력해야함
else:
    print(0)






'''