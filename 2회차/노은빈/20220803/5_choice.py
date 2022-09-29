#2864. 5와 6의 차이

a, b = input().split() #a와 b를 input 받음(map사용 X => 정수일 필요가 없음) str로 map 써도 됨

#replace는 문자열만 가능하기 때문
#AttributeError: 'int' object has no attribute 'replace'

min = int(a.replace('6', '5')) + int(b.replace('6', '5'))  
#6은 5로 바꾸고(5가 더 작기 때문에 최솟값)
max = int(a.replace('5', '6')) + int(b.replace('5', '6'))  
#5는 6으로 바꿈

print(min, max)  




