# 혜성이는 승엽이의 이모티콘을 귀여운 척이라고 생각해 매우 싫어하므로, 승엽이의 문자가 오면 전체적인 분위기만 판단해서 알려주는 프로그램을 작성하고 싶다.


# How are you :-) doing :-( today :-)?

# happy


s=input()   # 입력예제를 입력한다.
smile=s.count(":-)")    # 문자열에서 문자의 총 발생 횟수를 기록한다.
sad=s.count(":-(")  # 문자열에서 문자의 총 발생 횟수를 기록한다.
if smile==0 and sad==0: print("none")   # 카운트 된 문자열이 없으면 none 출력.
elif smile>sad: print("happy")  # 스마일 문자가 더 많으면 happy 출력.
elif smile==sad: print("unsure")    # 스마일과 새드 문자가 같다면 언슈얼 출력.
elif smile<sad: print("sad")    # 새드의 문자가 더 많으면 sad 출력.