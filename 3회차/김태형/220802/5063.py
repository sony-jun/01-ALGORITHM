# 광고 효과가 주어졌을 때, 광고를 해야할지 말아야할지 결정하는 프로그램을 작성하시오.
# 사칙연산

N = int(input())
for i in range(N):
    r,e,c=map(int,input().split())
    if e-r>c:
        print("advertise")
    elif e-r<c:
        print("do not advertise")
    else:
        print("does not matter")