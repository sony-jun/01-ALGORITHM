N = int(input())
yoso = []       # i를 일일이 뽑아내기위해 리스트를 만들어둠 (i를 요소하나하나 담아둘 통)
yoso2 = 0        # 요소들을 전부다 합한 값을 (자릿수를 다 합한값) 넣을 변수
for i in range(1, N + 1):  # N이하의 자연수를 순회
    for j in str(i):        # i는 숫자니까 순회가능하게 문자로변경
        yoso.append(int(j))         # 문자인 i를 다시 숫자로 바꿔줌. 즉 int(j) 는 각각의 자릿수임. 그걸 빈 리스트 yoso 에 추가함
        yoso2 = sum(yoso)           # 리스트에 i의 각각의 자릿수인 int(j)가 전부다 들어갔으니, 그걸 전부다 더해서, yoso2에 할당시킴.  (자릿수의 합)
    if N == i + yoso2:   # N이하의 자연수 i에 대하여 i + i의 자릿수 합이 처음 입력값 N과 같다면,
        print(i)         # i를 출력하고, 종료.
        break
    if i == N:          # i가 N까지 왔는데도 위의 조건을 만족시키는 i를 찾지못했다면, 0을 출력하고 종료.
        print(0)
    yoso2 = 0
    yoso = []           #이중 for문, for j 어쩌구에서 yoso와 yoso2의 값이 i가 하나하나 변할때마다 변하므로, i가 1씩 증가하기 직전에 yoso와 yoso2를 초기화시킴. 반복
    
    
    