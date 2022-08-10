#꼬리를  무는 숫자 (구글링함)

x, y = map(int,input().split()) #input 받기

x -= 1 #각 좌표의 -1한 값이 위치
y -= 1

#abs 절대값 함수 
w = abs(x//4 - y//4) # 2 - 8 = -6
h = abs(x % 4 - y % 4) # 3 - 1 = 2

print(w + h) # 더하면 두 수의 직각거리가 나옴
