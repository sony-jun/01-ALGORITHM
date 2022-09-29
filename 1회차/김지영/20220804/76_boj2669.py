rtg = [list(map(int,input().split())) for _ in range(4)]
print(rtg)
def ract(x1,y1,x2,y2):
    r_w = abs(x1-x2)
    r_h = abs(y1-y2)
    area = r_w * r_h
    
    return r_w, r_h, area
for y in range(4):
    x1,y1,x2,y2 = rtg[y][0],rtg[y][1],rtg[y][2],rtg[y][3]
# 슈도코드
    if rac1.x1< rac2.a and rac2.a <rac1.x2:
        x1 = rac2.x1
        y1 = rac2.y1
        x2 = rac1.x2
        y2 = rac1.y2
