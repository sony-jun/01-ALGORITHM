# 두 단어가 애너그램인지 아닌지 구하는 프로그램을 작성하시오.

import sys
sys.stdin = open("6996.txt")

# 애너그램 : 구성 알파벳이 같다 = 알파벳을 정렬했을 때 같은 단어인지 확인

N = int(input())
for i in range(N):
    a,b = input().split()
    A = sorted(a) # sorted 메소드 사용시 문자열이 분리되기때문에 다른 변수에 저장해서 배교
    B = sorted(b)
    if A==B:
        print(f"{a} & {b} are anagrams.")
    else:
        print(f"{a} & {b} are NOT anagrams.")