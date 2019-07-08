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
    MessageID = 2
    RepeatIndicator = bin_int(pp[6:8])
    UserID = bin_int(pp[8:38])
    NavigationStatus = bin_int(pp[38:42])
    ROT = bin_int(pp[42:50])
    SOG = bin_int(pp[50:60])
    PositionAccuracy = bin_int(pp[60:61])
    longitude = bin_int(pp[61:89])/600000
    latitude = bin_int(pp[89:116])/600000
    COG = bin_int(pp[116:128])
    TrueHeading =  bin_int(pp[128:137])
    TimeStamp = bin_int(pp[137:143])
    RegionalReserved = bin_int(pp[143:147])
    Spare = bin_int(pp[147:148])
    RAIM = bin_int(pp[148:149])
    state_syncstate = bin_int(pp[149:151])
    state_slottimeout = bin_int(pp[151:154])
    state_slotoffset = bin_int(pp[154:159])
    tt = ''
    for i in range(len(ss)):
        tt = tt + ',' + ss[i]

    return [tt, ss[0][0:10],MessageID, RepeatIndicator, UserID, NavigationStatus, ROT, SOG, PositionAccuracy, longitude, latitude, COG,TrueHeading, TimeStamp, RegionalReserved, Spare, RAIM, state_syncstate, state_slottimeout, state_slotoffset]
