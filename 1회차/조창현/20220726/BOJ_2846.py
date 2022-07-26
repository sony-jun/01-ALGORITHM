N = input()
slope = input().split()
slope_sum = 0
slope_num = [0]
#print(slope)

for i in range(0, int(N) - 1):
    ## int 만 있고 없고 차이로 왜지...
    if int(slope[i]) < int(slope[i+1]):
        #print(int(slope[i+1]) - int(slope[i]))
        slope_sum += int(slope[i+1]) - int(slope[i])
        slope_num.append(slope_sum)
    else:
        slope_sum = 0
print(max(slope_num))