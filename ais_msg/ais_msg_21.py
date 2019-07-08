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
    MessageID = 21
    RepeatIndicator = bin_int(pp[6:8])
    UserID = bin_int(pp[8:38])
    type = bin_int(pp[38:43])
    name = bin_int(pp[43:163])
    PositionAccuracy = bin_int(pp[163:164])
    longitude = bin_int(pp[164:192]) /600000
    latitude = bin_int(pp[192:219])/600000
    dimA = bin_int(pp[219:228])
    dimB = bin_int(pp[228:237])
    dimC = bin_int(pp[237:243])
    dimD = bin_int(pp[243:249])
    FixType = bin_int(pp[249:253])
    timestamp = bin_int(pp[253:259])
    OffPosition = bin_int(pp[259:260])
    status = bin_int(pp[260:268])
    RAIM = bin_int(pp[268:269])
    virtual_aton_flag = bin_int(pp[269:270])
    assigned_mode_flag = bin_int(pp[270:271])
    spare = 0
    tt = ''
    for i in range(len(ss)):
        tt = tt + ',' + ss[i]

    return [tt, ss[0][0:10],MessageID,RepeatIndicator ,UserID ,type ,name ,PositionAccuracy ,longitude ,latitude ,dimA,dimB ,dimC ,dimD,FixType ,timestamp ,OffPosition , status,RAIM,virtual_aton_flag ,assigned_mode_flag ,spare ]