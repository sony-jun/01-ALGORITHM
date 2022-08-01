from re import A
import sys

sys.stdin = open("06.배부른마라토너.txt")

N = int(input()) #참가자 수 입력 받아서
attend_list = list(map(int,input()))
# 참가자의 이름 입력받기(리스트)

'''INPUT값을 살펴보면, 3명의 참석자를 알려주고, 그 뒤에 완주자를 알려줘.
뒤에서 입력받지 못한 값이 : 탈락자. 인거지.
후에 입력받은 이름이 같은 값에 -1을 해주면 1인 사람이 탈락자. 
동명이인이 있을 수 있다<<라는 게 dictionary로만 저장하면 안되고 ,
defaultdict 로 해야한다는 거구나..'''


