n = int(input()) # 손님의 수 N이 주어짐
seat = map(int, input().split()) # 원하는 자리 정수형으로 변환
pc = [0]*101
reject_cus = 0 # 거절당하는 손님

for a in seat:
    if(pc[a] == 0): # 원하는 자리 비어있으면
        pc[a] += 1
    else:
        reject_cus += 1
        
print(reject_cus)