# 백준 최대공약수와 최소공배수  2609
# 두 개의 자연수를 입력받아 최대 공약수와 최소 공배수를 출력하는 프로그램을 작성하시오.



A, B = map(int, (input().split()))
for i in range(B, 0, -1):
    if A % i == 0 and B % i == 0:
        print(i)
        a = A // i
        b = B // i
        min_X = a*b*i
        print(min_X)
        break