# '''
# index A와 B가 1000을 넘지 않는다는 조건이 있기에 count를 실행하여 45이상의 값이 나올 수 없다는 걸 확인 후
# 반복횟수를 제한시키는 것이 제 최선이었습니다. 
# 이 하드 코딩을 해소할 방법을 논의 해보고 싶습니다.
# 인덱스 값의 제한 없이 풀 수 있는 방법이 있을 것 같습니다.
# '''
import math

A, B = map(int, input().split())
# def m_sequence(a):
#     cnt = 1
#     for i in range(1, 46):  
#         for j in range(i):
#             a.append(i)
#             cnt += 1
#             if cnt > 1000:
#                 return

# a = []
# m_sequence(a)
# print(sum(a[A-1:B]))

x=0
while B//A:
    x += math.sqrt( 2 * A ) + .5
    A += 1
print("%d"%x)