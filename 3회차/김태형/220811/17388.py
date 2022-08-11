import sys
sys.stdin = open("17388.txt")

# 동아리가 속한 대학의 영문 이름의 첫 단어를 출력한다.

# 대학별 참여도
S, K, H  = list(map(int,input().split()))
engage = S,K,H # 작성하기 쉽도록 다른 변수에 저장

sum_engage = sum(engage) # 참여도의 합

# 참여도의 합이 100 이하이면
if sum_engage<100:
# 참여도가 가장 작은 대학 지목 : 리스트에서 참여도의 최솟값과 비교
    if engage[0]==min(engage): 
        print("Soongsil")
    elif engage[1]==min(engage):
        print("Korea")
    else:
        print("Hanyang")
# 참여도의 합이 100 이상이면
else:
    print("OK")