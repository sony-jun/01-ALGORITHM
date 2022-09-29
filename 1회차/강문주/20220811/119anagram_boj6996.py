import sys
sys.stdin =open("boj4963.txt")
input = sys.stdin.readline

T = int(input())

for i in range(T):
    a, b = map(str,input().split())
    x = sorted(a)
    y = sorted(b) #정렬해서 

    if x == y:
        print(a, "&", b, "are anagrams.") #일치하면 anagram
    else:
        print(a, "&", b, "are NOT anagrams.")
        #a순서 바꿔서 b만들 수 있으면 anangram