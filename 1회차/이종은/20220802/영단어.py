# 네오가 프로도에게 숫자를 건넬 때 일부 자릿수를 영단어로 바꾼 카드를 건네주면 
# 프로도는 원래 숫자를 찾아야함 
num_s = {'zero':'0', 'one':'1', 'two':'2', 'three':'3', 'four':'4', 'five':'5', 'six':'6', 
             'seven':'7', 'eight':'8', 'nine':'9'}

def solution(s):
    answer = s

    
    for key, value in num_s.items():
        answer = answer.replace(key, value) # replace 주어진 문자열에서 key값에 들어간 것이 있으면 전부다 value값으로 교체 
        # 변수.replace(바뀔 것, 바뀐 것)
    return int(answer) # 문자열 -> 정수형으로 형변환