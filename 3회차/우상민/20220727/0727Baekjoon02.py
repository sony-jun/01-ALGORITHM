# 알파벳 대소문자로 된 단어가 주어지면, 이 단어에서 가장 많이 사용된 알파벳이 무엇인지 알아내는 프로그램을 작성하시오. 단, 대문자와 소문자를 구분하지 않는다.


N = list(input())

li = []
for i in range(len(N)):
    first_ = ord(str(N[i]))
    if first_ > 90:
        li.append(chr(first_-32))
    else:
        li.append(chr(first_))

count_ = {}
for idx in li:
    try: count_[idx] += 1
    except: count_[idx] = 1
MX = list(count_.values())
if MX.count(max(MX)) > 1:
    print('?')
else:
    result = max(count_, key = lambda k: count_[k])
    print(result)


