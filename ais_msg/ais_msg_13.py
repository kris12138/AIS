from ascii_table import ascii
def bin_int(tt):
    sum=0
    for i in range(len(tt)):
        sum+=int(tt[i])*(2**(len(tt)-1-i))
    return sum
def invert(ss):
    pp = ''
    for i in range(len(ss[6])):
        for j in range(len(ascii)):
            if ss[6][i] == ascii[j][1]:
                pp += ascii[j][2].replace('0b', '')
    MessageID = 13
    RepeatIndicator = bin_int(pp[6:8])
    UserID = bin_int(pp[8:38])
    Spare = 0
    DestID1 = bin_int(pp[40:70])
    SeqID1 = bin_int(pp[70:72])
    DestID2 = bin_int(pp[72:102])
    SeqID2 = bin_int(pp[102:104])
    DestID3 = bin_int(pp[104:134])
    SeqID3 = bin_int(pp[134:136])
    DestID4 = bin_int(pp[136:166])
    SeqID4 = bin_int(pp[166:168])
    tt = ''
    for i in range(len(ss)):
        tt = tt + ',' + ss[i]

    return [tt, ss[0][0:10],MessageID ,RepeatIndicator ,UserID ,Spare ,DestID1 ,SeqID1 , DestID2 , SeqID2 ,DestID3 ,SeqID3 ,DestID4 ,SeqID4 ]