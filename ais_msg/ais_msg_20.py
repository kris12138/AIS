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
    MessageID = 20
    RepeatIndicator = bin_int(pp[6:8])
    UserID = bin_int(pp[8:38])
    Spare = 0
    offset1 = bin_int(pp[40:52])
    numslots1 = bin_int(pp[52:56])
    timeout1 = bin_int(pp[56:59])
    increment1 = bin_int(pp[59:70])
    offset2 = bin_int(pp[70:82])
    numslots2 = bin_int(pp[82:86])
    timeout2 = bin_int(pp[86:89])
    increment2 = bin_int(pp[89:100])
    offset3 = bin_int(pp[100:112])
    numslots3 = bin_int(pp[112:116])
    timeout3 = bin_int(pp[116:119])
    increment3 = bin_int(pp[119:130])
    offset4 = bin_int(pp[130:142])
    numslots4 = bin_int(pp[142:146])
    timeout4 = bin_int(pp[146:149])
    increment4 = bin_int(pp[149:160])
    variablespare = 0
    tt = ''
    for i in range(len(ss)):
        tt = tt + ',' + ss[i]

    return [tt, ss[0][0:10],MessageID,RepeatIndicator,UserID ,Spare,offset1 ,numslots1 ,timeout1 ,increment1 ,offset2 ,numslots2 ,timeout2 ,increment2 ,offset3 ,numslots3,timeout3,increment3 ,offset4 ,numslots4,timeout4 ,increment4 ,variablespare ]