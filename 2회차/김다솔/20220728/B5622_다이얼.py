# https://www.acmicpc.net/problem/5622
# use dictionary! 

# 알파벳별로 걸리는 시간 딕셔너리 만들고 
# 키값으로 접근해서 구하기 

dict_ = {
    'A' : 2, 
}

time_ = 0 # 걸리는 시간 저장 

word = input()
for key in word:
    number = dict_[key]
    time_ += number + 1
    
print(time_)