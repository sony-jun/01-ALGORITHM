import sys

sys.stdin = open ("13_SASA.txt")

# 리스트로 만들어서 풀었을 경우 시간초과
# SASA를 문자의 갯수로 접근
# S가 2개 A가 2개 들어가야 SASA 문자 완성으로 1 출력
S, A = map(int, input().split()) # S는 4개 , A는 5개
print(min(S, A)//2)
# 문자의 갯수가 많아도 탈락되기 때문에 문자의 갯수가 적은 쪽을 기준으로 2를 나눠준다. (SASA에 알파벳이 쌍으로 들어가기 때문!)
