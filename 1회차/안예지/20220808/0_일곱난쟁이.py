# 2309.
"""
막힌 이유 : 7개 무작위 탐색을 '어떻게' 하나요?
일자형으로 탐색 하니까 7난쟁이의 키가 100을 만족하는 값이 안 나왔음.
일자로만 탐색할 수 있다고 생각한 사고 오류.

"""
n = 9
# cm = []
cm = ['20', '7', '23', '19', '10', '15', '25', '8', '13']
cm = list(map(int, cm))


for idx in range(len(cm)):
    cm_s = []
    for i in range(7):
        if 0<= idx <= 8:
            cm_s += [cm[idx]]
            idx += 1
        if idx > 8:
            
            if len(cm_s) == 7:
                if sum(cm_s) == 100:
                    print(cm_s)
        # if sum(cm_s[0:8]) == 100:
        #     print(cm_s)


        
        
    
            
    
    
