# https://www.acmicpc.net/problem/8958
# import sys
# sys.stdin = open("3_OX퀴즈.txt")

n=int(input())
for i in range(0,n):
    count,c=0,1
    s=list(input())
    for j in s:
        if j=='O':
            count+=c
            c+=1
        else:
            c=1
    print(count)

# 테스트케이스 수만큼 ox결과를 입력받는다.
# 입력받은 문자열은 list 함수를 이용해 문자로 분리해주었다.
# 해당 문자열이 O라면 count에 c를 더해준다.
# c는 문자열이 x라면 X로 초기화해주고, O라면 1씩 증가시켜 연속된 O의 개수를 구할 수 있도록 한다.

