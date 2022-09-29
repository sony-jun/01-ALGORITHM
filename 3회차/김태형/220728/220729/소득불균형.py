# n명의 사람의 소득이 주어졌을 때 이 중 평균 이하의 소득을 가진 사람들의 수를 출력해야 한다.

T = int(input())
N = int(input())
for i in range(1,N+1):
    n = list(map(int,input().split()))
    count_under = 0
    mean_num = sum(n)/len(n)
    for j in n:
        if j<=mean_num:
            count_under+=1
            print(count_under)
    print("#%d %d" %(i, count_under))