import sys
input = sys.stdin.readline

M = int(input())

cup = [0, 1, 2, 3]  
#0을 넣는 이유 : 값을 고정시키기 위해서 1,2,3외에 아무거나 넣어도 됨!!!
#0이 없으면 IndexError: list index out of range =>인덱스의 값으로 움직이기 때문에 0~3까지의 자리가 필요
for _ in range(M):
    a, b = map(int,input().split())
    cup[a], cup[b] = cup[b], cup[a]  
    # M이 2이고 1 2 , 3 1을 순서대로 받을 때
    #0 1 2 3
    #0 2 1 3
    #0 3 1 2

print(cup.index(1))  #처음 공을 넣은 컵의 위치
