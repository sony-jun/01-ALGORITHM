# https://school.programmers.co.kr/learn/courses/30/lessons/76501
# def solution(absolutes, signs):
answer = 0


absolutes = [1,2,3]
signs = [False,False,True]
p_li = [absolutes[i] for i in range(len(signs)) if signs[i] == True]
m_li = [absolutes[i] for i in range(len(signs)) if signs[i] == False]
# answer = sum(p_li) - sum(m_li)
print(p_li, m_li)   

# print(answer)