# 두 자연수 사이의 직각거리를 구하는 프로그램을 작성하시오.

# a, b = map(int,input().split())
# l = [[] for i in range(b//4+1)]
# i=0
# for j in range(1,b+1):
#     l[i].append(j)
#     if j%4==0:
#         i+=1

# for i in l:
#     for j in i:
#         if j==a:
#             x1=l.index(i)+1
#             y1=i.index(a)+1
#         if j==b:
#             x2=l.index(i)+1
#             y2=i.index(b)+1
# d = abs(x2-x1)+abs(y2-y1)
# print(d)


a, b = map(int,input().split())
x1 = a//4
y1 = a%4
x2 = b//4
y2 = b%4
d = abs(x2-x1)+abs(y2-y1)
print(d)