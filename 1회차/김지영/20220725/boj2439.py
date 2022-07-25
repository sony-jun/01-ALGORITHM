# 1부터 입력된 정수만큼 *을 찍는 프로그램
# 그런데 오른쪽 정렬을 곁들인...예상 : rstrip()
n = int(input())
for i in range(1,n+1):
    print(('*'*i).rjust(n))