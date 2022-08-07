cup = [1,2,3,4] # index = 0,1,2,3
swp = int(input()) # 몇번 섞을래?

for _ in range(swp):
    f,s = map(int,input().split()) # first input,second input
 # 처음 공의 위치
    f,s = cup.index(f),cup.index(s) # index로 전환
    cup[f],cup[s] = cup[s],cup[f] # swap
    # print(cup)
print(cup[0])