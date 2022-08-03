# 분해합
# N과 N을 이루는 각 자리수의 합
# M의 분해합이 N이면 M은 N의 생성자
# if N = 256(=245+2+4+5) M = 245
N = int(input())
# 생성자 M은 N보다 작은 어떤 수..
# 가장 작은 생성자 M이라...
# 1부터 N까지 진행해서 생성자가 있으면 M을 출력
for M in range(1,N+1):
    sepM = list(map(int,str(M))) # M의 자리수를 구하기 위한 sepM
    if M+sum(sepM) == N:
        print(M)
        break
    # 생성자가 없는 경우? = M이 N까지 진행하게 되겠지..
    if M == N:
        print(0)
        break