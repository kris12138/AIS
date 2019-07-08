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
    MessageID = 15
    RepeatIndicator = bin_int(pp[6:8])
    UserID = bin_int(pp[8:38])
    Spare0 = 0
    DestID = bin_int(pp[40:70])
    MessageID1 = bin_int(pp[68:74])
    SlotOffset = bin_int(pp[74:86])
    Spare1 = 0
    MessageID12 = bin_int(pp[88:94])
    SlotOffset12 = bin_int(pp[94:106])
    Spare2 = 0
    DestID2 = bin_int(pp[108:138])
    MessageID2 = bin_int(pp[138:144])
    SlotOffset2 = bin_int(pp[144:156])
    Spare3 = 0
    tt = ''
    for i in range(len(ss)):
        tt = tt + ',' + ss[i]

    return [tt, ss[0][0:10],MessageID ,RepeatIndicator ,UserID ,Spare0 ,DestID , MessageID1 , SlotOffset ,Spare1 ,MessageID12 ,SlotOffset12 ,Spare2 ,DestID2 , MessageID2 ,SlotOffset2 ,Spare3  ]