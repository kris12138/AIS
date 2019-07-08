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
    MessageID = 10
    RepeatIndicator = bin_int(pp[6:8])
    UserID = bin_int(pp[8:38])
    Spare1 = 0
    DestID = bin_int(pp[40:70])
    Spare2 = 0
    tt = ''
    for i in range(len(ss)):
        tt = tt + ',' + ss[i]

    return [tt, ss[0][0:10],MessageID ,RepeatIndicator , UserID ,Spare1 , DestID ,Spare2 ]