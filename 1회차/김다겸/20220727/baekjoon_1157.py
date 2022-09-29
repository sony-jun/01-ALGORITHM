# word 입력 받기
word = input()
# word를 모두 대문자로 변경
WORD = word.upper()

# 알파벳 나온 횟수 저장할 리스트 0으로 초기화
list = [0] * 27
# 답 넣을 리스트 선언
answer = []

# WORD를 순회
for i in WORD:
    # WORD에서 한글자씩 아스키 코드로 변환 후 
    # 64를 빼서 A가 1부터 시작할 수 있도록
    asci = ord(i) - 64

    # 아스키코드가 해당하는 인덱스에 1씩 더함
    list[asci] += 1

# list 순회
for i in range(len(list)):
    # 만약 list의 값이 list의 최댓값과 같다면
    if list[i] == max(list):
        # answer 리스트에 해당 값을 문자로 변환후 추가
        answer.append(chr(i+64))

# 만약 answr의 갯수가 2보다 크거나 같으면
if len(answer) >= 2:
    # ? 출력
    print("?")
# 만약 answer의 갯수가 1개면
else:
    # answer에 있는 알파벳 출력
    print(*answer)