import sys
sys.stdin = open("2. 와글와글 숭고한.txt", "r")

input = sys.stdin.readline

s,k,h = map(int,input().split())
sum = s+k+h
if sum >= 100:
    print('OK')
else:
    if s < k and s < h: # 숭실대가 고려대,한양대보다 작으면
        print('Soongsil') # 숭실.
    elif k < s and k < h: # 고려대가 숭실대,한양대보다 작으면
        print('Korea')  # 고려
    elif h < s and h < k: # 한양대가 숭실, 고려대보다 작으면
        print('Hanyang') # 한양