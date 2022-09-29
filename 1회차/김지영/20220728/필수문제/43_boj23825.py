# SASA?
# S블록 N개, A블록 M개
# SASA만들고싶어, 몇세트? S 두개, A 두개
# N//2,M//2 둘 중 작은 수
n,m = map(int,input().split())
s_n = n//2
a_m = m//2
if s_n>=a_m:
    print(a_m)
else : print(s_n)