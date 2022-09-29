#https://www.acmicpc.net/problem/1157
#문제)) 단어에서 많이 쓴 알파벳 출력하되 많이 쓴 게 여러 개 인경우에는 '?' 출력하기

#------
#대소문자 구분 안함 > 전부다 대문자 아니면 소문자로 만들어서 처리하자
#문자열 중복제거 해서 사용된 문자열 확인하고
#반복문으로 해당 알파벳의 사용빈도 확인
#알파벳 사용빈도 비교해서 최댓값 1개면 출력하고 2개 이상이면 물음표출력

word = input().upper() 
#문자열 받을 때 부터 대소문자 구분 제거 -> 전부 대문자로 만들기
apb = list(set(word))

cnt_list = []

for i in apb:
    #각 알파벳 사용빈도 count로 확인 후 cnt list에 저장
    cnt = word.count(i)
    cnt_list.append(cnt)

if cnt_list.count((max(cnt_list))) > 1:
    #최댓값이 중복될 경우 2개 이상이므로 물음표출력
    print('?')

else:
    #최댓값이 하나일 경우 해당 최댓값 인덱스로 찾아서 반환
    #cnt에 넣은 값이 word에서 해당 알파벳이 몇번 나오는지 세서 넣은 값이니까 해당 값의 인덱스 찾아서 apb[인덱스]로 반환하면 해당 알파벳을 얻을 수 있음
    print(apb[(cnt_list.index(max(cnt)))])