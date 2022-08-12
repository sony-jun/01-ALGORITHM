import sys


sys.stdin = open("input.txt")

# 호가 보기에 세 대학교의 참여도의 합이 100 이상이면 일처리가 잘 되고 있기에 안심할 수 있지만,
#  100 미만이면 창호는 참여도가 가장 낮은 대학의 동아리에게 무언의 압박을 넣을 예정이다. 
# 숭고한 알고리즘 캠프의 성공을 빌며 창호의 고민을 해결해주자.

# 입력
# 첫 번째 줄에 숭실대학교의 참여도, 고려대학교의 참여도,
#  한양대학교의 참여도를 의미하는 세 자연수 S, K, H가 공백으로 구분되어 주어진다.
#  (0 ≤ S, K, H ≤ 100)

# 세 대학의 참여도는 모두 다르다.

S, K, H = map(int,input().split())
sum_ = S+H+K


# S K H의 합이 100이랑 같거나 크다면
if  sum_ >= 100:
    #  OK
    print('OK')
else:
    # 만약 S K H 중 최소값이 S랑 같다면
    if S == min(S, K, H):
        # 숭실
        print("Soongsil")
        # K랑 같다면
    elif K == min(S, K, H):
        # KOREA
        print("Korea")
    else:
        # 나머지는 HANYANG
        print("Hanyang")