# https://www.acmicpc.net/problem/2908
import sys
# 상근이의 동생 상수는 수학을 정말 못한다. 상수는 숫자를 읽는데 문제가 있다. 
# 이렇게 수학을 못하는 상수를 위해서 상근이는 수의 크기를 비교하는 문제를 내주었다. 
# 상근이는 세 자리 수 두 개를 칠판에 써주었다. 그 다음에 크기가 큰 수를 말해보라고 했다.
A,B = map(int,input().split())
# 두개의 정수입력받기
if A > B:
    print(int(str(A)[::-1])) # A>B보다 클때 A를 슬라스하여 역순으로 출력한다
elif A < B:
    print(int(str(B)[::-1])) 
    #근데 왜 맨뒤에 숫자가 0이면 생략될까.......................???????

    
        

    

# 상수는 수를 다른 사람과 다르게 거꾸로 읽는다. 예를 들어, 734와 893을 칠판에 적었다면, 
# 상수는 이 수를 437과 398로 읽는다. 따라서, 상수는 두 수중 큰 수인 437을 큰 수라고 말할 것이다.

# 두 수가 주어졌을 때, 상수의 대답을 출력하는 프로그램을 작성하시오.
sys.stdin = open("1_상수.txt")
