# 동규가 연종이에게 M개의 질문을 던짐.
# 질문은 X라는 정수를 오늘 본 적이 있어? 라고.
# 연종이 봤다고 주장하는 수 들을 수첩 2에 적어두었다.

# 수첩2에 적혀있는 순서대로 수첩1에 있으면 1을 없으면 O을
# 집합형이면 set으로 구현. set객체는 순서 없는 교집합,합집합,차집합,수학연산 계산.
# 집합은 원소의 위치나 삽입 순서를 기록하지 않음.
# 인덱싱, 슬라이싱 또는 기타 시퀀스와 유사한 동작을 지원하지 않음.

from re import A
import sys

sys.stdin = open("암기왕.txt")


input = sys.stdin.readline
M = int(input())

for i in range(M):
    N = int(input())
    num1 = set(map(int,input().split()))
    m = int(input())
    num2 = list(map(int,input().split()))
    for num in num2:
        if num in num1:
            print(1)
        else:
            print(0)

#######런타임 에러뜸.... input값도 readline으로 바꾸고, 
#set으로 했는데 알고리즘분류에 해시를 이용한 집합과 맵<<이게 있는데, 
# 이걸 안한거같은데.....
