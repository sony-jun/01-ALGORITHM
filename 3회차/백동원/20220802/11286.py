import heapq

T = int(input())
minus_numbers = []    # 핵심은 음수와 양수를
plus_numbers = []     # 분리하여 보관하는 것
result = []           # 출력용 리스트          

for _ in range(T):                  
    a = int(input())
    if a > 0:                                   # 입력값이 양수이면
        heapq.heappush(plus_numbers, a)         # 양수 리스트에 저장
    elif a < 0:                                 # 음수이면 절대값 씌운 후 음수리스트에 저장
        heapq.heappush(minus_numbers, abs(a))   # (출력 시 절대값이 가장 적은 수를 출력하기 위함)
    else:                                       # 입력값이 0 일때
        if len(minus_numbers) + len(plus_numbers) == 0:             # 두 리스트에 아무것도 없다면,
            result.append(0)                                        # 출력용 리스트에 0 추가
        elif (len(minus_numbers) == 0) or (len(plus_numbers) == 0): # 두 리스트중 하나라도 비었을 때,
            if len(minus_numbers) == 0:                             # 그 빈 리스트가 음수 리스트라면,
                result.append(heapq.heappop(plus_numbers))          # 출력용 리스트에 양수 리스트에서 가장 적은 수 추가
            else:                                                   # 빈 리스트가 양수 리스트라면,
                result.append(-heapq.heappop(minus_numbers))        # 음수 리스트에서 가장 적은 수를 음수 형태로 출력용 리스트에 추가
        else:                                           # 두 리스트 모두 데이터를 가지고 있다면,
            plus_ = heapq.heappop(plus_numbers)         # 두 리스트에서 작은 데이터를 하나씩 뽑아 비교
            minus_ = heapq.heappop(minus_numbers)
            if  plus_ < minus_ :                        # 양수 데이터가 음수 절대값 데이터보다 작다면
                result.append(plus_)                    # 출력용 리스트에 양수 데이터 추가
                heapq.heappush(minus_numbers, minus_)   # 그 후 음수 리스트에서 뽑은 값을 다시 음수 리스트에 추가
            else:                                       # 음수 절대값 데이터가 양수 데이터 보다 작거나 같다면,
                result.append(-minus_)                  # 출력용 리스트에 음수 절대값 데이터를 음수형태로 추가
                heapq.heappush(plus_numbers, plus_)     # 그 후 양수 리스트에서 뽑은 값을 다시 양수 리스트에 추가
                
for a in result:        # 순서대로 출력
    print(a)