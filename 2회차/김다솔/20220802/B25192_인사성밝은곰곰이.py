import sys
sys.stdin = open('B25192.txt')
"""
중복된 닉네임이 있으냐 없으냐 !
set 이용, 
set.add()
set.clear()
"""

set_ = set()
for log in log_list:
    if log == 'ENTER':
        set_.clear()
        
    else:
        if log not in set_:
            set_.add(log)
            gon += 1
print(gom)

# 리스트에서 중복을 탐색할 때 n만큼의 시간필요.
# 셋은 1만큼만 필요. 