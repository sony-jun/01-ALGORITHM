from re import A
import sys

sys.stdin = open("43.세로읽기.txt")

numbers = [input() for i in range(5)] #오늘 오전에 배운 리스트 컴프리핸션.
for _ in range(5): #단어를 입력받은 후 단어의 길이도 함께 저장해보고.
    
