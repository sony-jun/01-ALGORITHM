from re import A
import sys

sys.stdin = open("수정렬하기.txt")

n = int(input())

numbers = []
for i in range(n): #for문을 이용하여 n개의 숫자들을 리스트에 담기.
    numbers.append(int(input())) #numbers list에 

numbers.sort() #sort() 함수를 이용하여 오름차순 정렬

for i in numbers:
    print(i)

    # sort는 리스트형의 메소드. 원본값을 수정함 : 리스트명.sort()
    # sorted는 내장함수, 원본값은 그대로이며 정렬한 값을 반환함. sorted(리스트명)