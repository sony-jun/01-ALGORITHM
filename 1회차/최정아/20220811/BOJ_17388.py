S, K, H = map(int, input().split())
d = {S: "Soongsil", K: "Korea", H: "Hanyang"}
if sum(d) >= 100: # 세 대학교의 합이 100 이상이면 
    print("OK") # OK 출력
else:
    print(d[min(d)]) # 참여도가 가장 낮은 대학의 동아리 출력