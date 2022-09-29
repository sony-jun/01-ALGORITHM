# 다섯 개의 자연수가 주어질 때 이들의 평균과 중앙값을 구하는 프로그램을 작성하시오.

n=[]
for i in range(5):
    d=int(input())
    n.append(d)
n=sorted(n)
avg = sum(n)//len(n)
mid = n[2]
print(avg)
print(mid)
