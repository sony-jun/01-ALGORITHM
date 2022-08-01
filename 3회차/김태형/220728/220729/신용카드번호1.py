# 16자리의 카드 번호 중 처음 15개가 주어졌을 때 룬 공식을 만족하기 위해 마지막에 들어가야하는 숫자N을 구하는 프로그램을 작성하시오.

T = int(input())
odd_num = 0
even_num = 0
for i in range(1,T+1):
    n = list(map(int,input().split()))
    odd_num = 2*(n[0]+n[2]+n[4]+n[6]+n[8]+n[10]+n[12]+n[14])
    even_num = n[1]+n[3]+n[5]+n[7]+n[9]+n[11]+n[13]
    sum_num = odd_num+even_num
    if sum_num%10==0:
        print("#%d %d" %(i,0))
    else:
        print("#%d %d" %(i, 10-sum_num%10))