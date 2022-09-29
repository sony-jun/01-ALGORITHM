# 0을 담은 리스트를 모든 좌표가 100이하라고 했으니 만들어줌 사각형의 면적을 체크하기 위한 용도
rec = [[0] * 100 for _ in range(100)]

#문제에서 요구하는 4개의 도형을 돈다.
for _ in range(4):
    #입력값을 받는다.
    x1, y1, x2, y2 = map(int, input().split())
    #꼭짓점좌표를 활용해주려면 -1을 해야하지만 range에 +1을 하지 않으면 똑같은 효과가 일어난다.
    for i in range(x1, x2):
        for j in range(y1, y2):
            #아무값도 없는 x,y평면에 사각형이 한 번이라도 면적에 속하면 1을 대입한다.
            rec[i][j] = 1

#map 함수를 활용해서 리스트의 모든 요소를 더한 값을 합해준다.  
print(sum(map(sum, rec)))
