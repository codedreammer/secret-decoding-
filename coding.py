st = input("Enter message ")
words = st.split(" ")
coding = True
if (coding):
    nwords = []
    for word in words:
        if(len(word)>=3):
            r1 = "dsf"
            r2 = "jkf"
            stnew = r1+ word[1:] + word[0] + r2
            nwords.append(stnew)
        else:
            nwords.append(word[::-1])
    print(" ".join(nwords))

