# https://www.acmicpc.net/problem/23825

n, m = map(int,input().split())
s, a = n//2, m//2   # S와 A블록 2개씩 필요하므로 개수 n,m을 2로 나눴을 때 몫을 구한다.
print(min(s, a))    # SASA 모형을 만들기 위해서 둘 중에 적은 블록 개수를 구한다.
