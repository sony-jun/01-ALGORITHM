import sys
sys.stdin = open("Anagrams.txt")

t = int(input()) #테스트 케이스

for i in range(t): 
    a,b = list(map(str,input().split())) #a,b를 리스트로 받음(정렬하기 위해서)

    aa = sorted(a) #리스트를 정렬해서 비교
    bb = sorted(b)
# print(aa)
# print(bb)

    if aa == bb:
        print('%s & %s are anagrams.' %(a,b)) #%s 문자열
    else : 
        print('%s & %s are NOT anagrams.'%(a,b))

