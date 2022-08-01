# 카드 번호가 주어졌을 때 해당 번호로 신용카드를 만들 수 있는지 판별하는 프로그램을 작성하시오.

T = int(input())
for i in range(1,T+1):
    n=input()
    n=n.replace("-","")
    if int(n[0]) in [3,4,5,6,9] and len(n)==16:
        print("#%d %d" %(i, 1))
    else:
        print("#%d %d" %(i, 0))