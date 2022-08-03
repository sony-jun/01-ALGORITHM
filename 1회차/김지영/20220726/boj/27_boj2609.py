# 두개의 자연수 입력
# 최대 공약수와 최소 공배수 출력
a,b = map(int,input().split())
# 약수는 어떻게 구하지...
# a,b를 1~n까지 다 나눠서 0나오는 애들만 모아볼까?

# 약수는 어떻게 구할까요.
# n을 1부터 n까지의 수로 나눠서 0이 나오는 애들이겠죠
def Mlst(n):
    lst=[]
    for i in range(1,n+1):
        if n % i == 0:
            lst.append(i)
    return lst
# 큰수 작은수 비교 없이 하면 아마 리스트 요소를 비교하는 이중 for문을 써야할거에요.
# for문을 덜 돌리려면 a,b 중에 작은 수를 구하는게 낫겠다.

# 최대공약수는 큰수를 작은 수의 약수들로 나눠 0이 나오는 것들 중에 제일 큰 값을 받으면 되겠죠
# 그래서 나눌때 리스트를 역순으로 읽을 거에요.

# 공배수는 어떻게 구할까요..
# a*b를 곱한건 무조건 공배수가 되겠죠.
# 그러면 큰수에다 1부터 작은 수까지의 수들을 곱할건데. 
# 그 곱해서 나온 수를 작은 수로 나눴을때 0이 나오면 break을 걸고 출력하면 되겠다!
# 큰 수 작은수 구분은 위에서 했으니 거기에다 같이 쓸게요
if a > b:                       # a가 b보다 클때
    b_Mlst = Mlst(b)            # 작은 수인 b의 약수를 구해서
    for i in b_Mlst[::-1]:      # 약수를 역순으로 읽으면서
        if a % i == 0 :         # a를 약수로 나눠볼게요
            print(i)            # 그래서 나눠떨어지면 출력하고 멈출게요
            break
    for i in range(1,b+1):      # 1부터 b까지의 수를 큰 수인 a에다 곱해볼게요
        mul = a * i             
        if mul % b == 0:        # 그래서 나온 수가 작은 수인 b로 나눠떨어지면
            print(mul)          # 출력하고 멈출게요.
            break
if a < b:
    a_Mlst = Mlst(a)
    for i in a_Mlst[::-1]:
        if b % i == 0 :
            print(i)
            break
    for i in range(1,a+1):
        mul = b * i
        if mul % a == 0:
            print(mul)
            break
if a == b:
    print(a)
    print(a)
# 시간 = 3 * O(N) = O(N)