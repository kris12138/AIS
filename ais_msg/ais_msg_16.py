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
    MessageID = 16
    RepeatIndicator = bin_int(pp[6:8])
    UserID = bin_int(pp[8:38])
    Spare0 = 0
    DestIDA = bin_int(pp[40:70])
    SlotOffsetA = bin_int(pp[70:82])
    IncrementA=bin_int(pp[82:92])
    DestIDB=bin_int(pp[92:122])
    SlotOffsetB = bin_int(pp[122:134])
    IncrementB = bin_int(pp[134:144])
    Spare1 = 0

    tt = ''
    for i in range(len(ss)):
        tt = tt + ',' + ss[i]

    return [tt, ss[0][0:10],MessageID ,RepeatIndicator ,UserID ,Spare0 , DestIDA , SlotOffsetA ,IncrementA,DestIDB,SlotOffsetB ,IncrementB ,Spare1 ]