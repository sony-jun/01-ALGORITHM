# 1157
#알파벳 대소문자로 된 단어가 주어지면, 이 단어에서 가장 많이 사용된 알파벳이 무엇인지 알아내는 프로그램을 작성하시오. 단, 대문자와 소문자를 구분하지 않는다.
danuh = input().upper()
max_ = list(set(danuh))
list_ = []
for i in max_:
    cnt = danuh.count(i)
    list_.append(cnt)
    
if list_.count(max(list_)) > 1:
    print('?')
else:
    max_index = list_.index(max(list_))
    print(max_[max_index])     