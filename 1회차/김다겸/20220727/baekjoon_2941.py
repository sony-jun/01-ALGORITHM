# word 입력
word = input()

# word에 "c="가 있으면 "_"로 변환 후 word_c에 저장
word_c = word.replace("c=", "_")
# word_c에 "c-"가 있으면 "_"로 변환 후 word_c2에 저장
word_c2 = word_c.replace("c-", "_")
# word_c2에 "dz="가 있으면 "_"로 변환 후 word_dz에 저장
word_dz = word_c2.replace("dz=", "_")
# word_dz에 "d-"가 있으면 "_"로 변환 후 word_d에 저장
word_d = word_dz.replace("d-", "_")
# word_d에 "lj"가 있으면 "_"로 변환 후 word_lj에 저장
word_lj = word_d.replace("lj", "_")
# word_lj에 "nj"가 있으면 "_"로 변환 후 word_nj에 저장
word_nj = word_lj.replace("nj", "_")
# word_lj에 "s="가 있으면 "_"로 변환 후 word_s에 저장
word_s = word_nj.replace("s=", "_")
# word_s에 "z="가 있으면 "_"로 변환 후 word_z에 저장
word_z = word_s.replace("z=", "_")

# word_z 출력
print(len(word_z))