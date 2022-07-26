# 자전거 등교
# 길 종류: 오르막, 내리막, 평지

def boj_2846():
    N = int(input())
    N_list = list(map(int, input().split()))
    upper_road = []
    height_upper = []
    upper_start = -1

    for i in range(N):
        if i < N-1:
            if N_list[i+1] - N_list[i] > 0:
                upper_road.append(i)
                if upper_start == -1:
                    upper_start = i
        else:
            if N_list[i] - N_list[i-1] > 0:
                upper_road.append(i)
                if upper_start == -1:
                    upper_start = i
        
        if upper_start != -1:     
            if i < N-1:
                if N_list[i+1] - N_list[i] <= 0:
                    height_upper.append(N_list[i]-N_list[upper_start])
                    upper_start = -1
            else:
                if N_list[i] - N_list[i-1] <= 0:
                    height_upper.append(N_list[i-1]-N_list[upper_start])  
                    upper_start = -1
                else:
                    height_upper.append(N_list[i]-N_list[upper_start])  
                    upper_start = -1

    if upper_road == []:
        print(0)
        return
    
    print(max(height_upper))

boj_2846()
    