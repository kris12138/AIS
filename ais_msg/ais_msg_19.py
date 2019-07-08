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
    MessageID = 19
    RepeatIndicator = bin_int(pp[6:8])
    UserID = bin_int(pp[8:38])
    Spare = 0
    SOG = bin_int(pp[46:56])
    PositionAccuracy = bin_int(pp[56:57])
    longitude =bin_int(pp[57:85]) /600000
    latitude = bin_int(pp[85:112]) / 600000
    COG = bin_int(pp[112:124])
    TrueHeading = bin_int(pp[124:133])
    TimeStamp = bin_int(pp[133:139])
    Spare2 = 0
    name = bin_int(pp[143:263])
    shipandcargo = bin_int(pp[263:271])
    dimA = bin_int(pp[271:280])
    dimB = bin_int(pp[280:289])
    dimC = bin_int(pp[289:295])
    dimD = bin_int(pp[295:301])
    fixtype = bin_int(pp[301:305])
    RAIM = bin_int(pp[305:306])
    DTE = bin_int(pp[306:307])
    Spare3 = 0
    tt = ''
    for i in range(len(ss)):
        tt = tt + ',' + ss[i]

    return [tt, ss[0][0:10],MessageID,RepeatIndicator ,UserID,Spare , SOG,PositionAccuracy ,longitude,latitude ,COG ,TrueHeading ,TimeStamp ,Spare2,name ,shipandcargo ,dimA ,dimB ,dimC ,dimD ,fixtype,RAIM ,DTE ,Spare3 ]