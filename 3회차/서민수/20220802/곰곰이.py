# if 닉네임 not in set: 입력 닉네임이 셋에 없을 떄 
# set. add() # 추가
# 곰 += 1

# 기존에 있던 걸 지워줘
# if 닉네임 == enter
# set.clear()

N = 7
gom = 0

log_list ={
        "ENTER",
        "pjshwa",
        "cjhasol",
        "chogahui05",
        "ENTER",
        "pjshwa",
        "chansol"
}

set_ = set()

for log in log_list:
    if log =="ENTER":
        set_.clear()

    else:
        # 닉네임 = log
        if log not in set_:
            set_.add(log)
            gom += 1
print(gom)