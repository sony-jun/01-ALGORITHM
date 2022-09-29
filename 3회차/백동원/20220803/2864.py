# 5와 6의 차이

A, B = input().split()
a = A
b = B
min_ = int(a.replace('6', '5')) + int(b.replace('6', '5'))
max_ = int(A.replace('5', '6')) + int(b.replace('5', '6'))
print(min_, max_)