def upr_4(str):
    return str == str[::-1]

def upr_14(str):
    s = str.split()
    count_word = 0
    for i in range(len(s)):
        word = s[i]
        cnt = 0
        for c in word:
            if c=='e':
                cnt += 1
        if cnt == 3:
            count_word+=1

    return count_word

print(upr_4("потоп")) #true
print(upr_4("зонтик")) #false

print(upr_14("elkvnee celkene kmfkoign jvofnkfn knsinxcnfeee vfvfikneenn")) #3