def solution(s):
    nums={'0':'zero','1':'one','2':'two','3':'three','4':'four','5':'five','6':'six','7':'seven','8':'eight','9':'nine'}
    for k,v in nums.items():
        if v in s:
            s=s.replace(v,k)
    answer = int(s)
    return answer

print(solution("23four5six7"))
    