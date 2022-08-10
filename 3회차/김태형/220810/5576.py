# 각각의 대학의 점수를 계산하는 프로그램을 작성하라.
# 20개 : 10
l=[]
for i in range(20):
    n = int(input())
    l.append(n)
A = l[0:10]
B = l[10:20]
A.sort(reverse=True)
B.sort(reverse=True)
print(sum(A[0:3]))
print(sum(B[0:3]))