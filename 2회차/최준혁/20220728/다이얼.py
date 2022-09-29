import sys

s = sys.stdin.readline()
a = {
    3:["A", "B", "C"], 4:["D", "E", "F"], 5:["G", "H", "I"],
    6:["J", "K", "L"], 7:["M", "N", "O"], 8:["P", "Q", "R", "S"],
    9:["T", "U", "V"], 10:["W", "X", "Y", "Z"]
    }
cnt = 0

for i in s: # 입력한 값
    for j, k in a.items(): # items()로 키와 값을 가져옴
        if i in k: # Value 안에 입력값이 포함되어있으면
            cnt += j # 키를 누적
print(cnt)
