n = input()

#마지막에 제거한 나머지 알파벳들을 세기 위해 count2 set생성
count2 = set()

# coratia 리스트에 해당 알파벳이 몇개 들어있는지 세기 위해 count = 0으로 초기화
count = 0

#크로아티아 알파벳 리스트 생성
croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

#입력한 n에서 알파벳이 몇개 있는지 세고 제거함
for i in croatia:
    if i in n:
        count += 1
        n = n.replace(i,'')
print(n)

#남은 알파벳들을 중복없이 세기 위하여 set에 추가하여 길이를 구함
for j in n:
    count2.add(j)
print(len(count2)+count)