# 이 문자열을 거울에 비추면 어떤 문자열이 되는지 구하는 프로그램을 작성하라.

T = int(input())
for i in range(1,T+1):
    s=input()
    s=s[::-1]
    s=s.replace("b","d")
    s=s.replace("p","q")
    print("#%d %s" %(i,s))