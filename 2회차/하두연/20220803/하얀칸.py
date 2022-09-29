# 백준 1100

# 체스판은 8×8크기이고, 검정 칸과 하얀 칸이 번갈아가면서 색칠되어 있다. 가장 왼쪽 위칸 (0,0)은 하얀색이다. 체스판의 상태가 주어졌을 때, 하얀 칸 위에 말이 몇 개 있는지 출력하는 프로그램을 작성하시오.


chess = []

for _ in range(8):
    chess.append(list(map(str,input())))        # 리스트에 2차원배열 만들기

cnt = 0                                                 # F의 수를 셀 변수

for i in range(8):
     for j in range(8):
         if chess [i][j] == 'F':                         # 말이 있는 칸 
             if (i + j) % 2 == 0:                        # 하얀칸을 짝수로 보고 짝수 일 시 하얀칸인걸 체크
                 cnt += 1                                # F가 있으면 1을 증가시키고 카운트에 체크

print(cnt)                                               # 카운트 출력, list index out of range 오류 발생.. 
                                                         # input 뒤에 split을 지우니 해결이 됨