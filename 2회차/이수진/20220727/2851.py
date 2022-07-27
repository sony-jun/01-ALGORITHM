currentScore=0
nextScore=0
for i in range(10):
    nextScore=int(input())
    c_gap=100-currentScore # 100
    n_gap=100-(currentScore+nextScore) #99
    if c_gap < 0 :
        c_gap=-(c_gap)
    if n_gap < 0 :
        n_gap=-(n_gap)
    if c_gap < n_gap :
        print(currentScore)
        break
    if c_gap >= n_gap :
        currentScore+=nextScore

else : print(currentScore)
