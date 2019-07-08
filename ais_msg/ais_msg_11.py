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
    MessageID=11
    RepeatIndicator=bin_int(pp[6:8])
    UserID=bin_int(pp[8:38])
    Time_year=bin_int(pp[38:52])
    Time_month=bin_int(pp[52:56])
    Time_day=bin_int(pp[56:61])
    Time_hour=bin_int(pp[61:66])
    Time_min=bin_int(pp[66:72])
    Time_sec=bin_int(pp[72:78])
    PositionAccuracy=bin_int(pp[78:79])
    Position_longitude=bin_int(pp[79:107])/600000
    Position_latitude=bin_int(pp[107:134])/600000
    fixtype=bin_int(pp[134:138])
    Spare=0
    RAIM=bin_int(pp[148:149])
    state_syncstate=bin_int(pp[149:151])
    state_slottimeout=bin_int(pp[151:154])
    state_slotoffset=bin_int(pp[154:168])
    tt = ''
    for i in range(len(ss)):
        tt = tt + ',' + ss[i]

    return [tt, ss[0][0:10],MessageID,RepeatIndicator,UserID,Time_year,Time_month,Time_day,Time_hour,Time_min,Time_sec,PositionAccuracy,Position_longitude,Position_latitude,fixtype,Spare,RAIM,state_syncstate,state_slottimeout,state_slotoffset]