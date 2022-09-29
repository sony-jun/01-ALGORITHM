def re_verse(number):
#re_verse 함수 정의
    lst = []
#빈 리스트 생성
    number = str(number)
#int형을 str형으로 변경
    for num in number:
        lst.append(num)
#리스트에 str을 추가
    lst.reverse()
#reverse() 사용
    number = ''.join(lst)
# join사용
    number= int(number)
#int형으로 변환
    return number

a, b = map(int,input().split())

sum = re_verse(a) + re_verse(b)
print(re_verse(sum))



