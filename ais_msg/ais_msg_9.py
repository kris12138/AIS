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
    MessageID = 9
    RepeatIndicator = bin_int(pp[6:8])
    UserID = bin_int(pp[8:38])
    Altitude = bin_int(pp[38:50])
    SOG = bin_int(pp[50:60])
    PositionAccuracy = bin_int(pp[60:61])
    Position_longitude = bin_int(pp[61:89])/600000
    Position_latitude = bin_int(pp[89:116])/600000
    COG = bin_int(pp[116:128])
    TimeStamp = bin_int(pp[128:134])
    Reserved = 0
    DTE = bool(bin_int(pp[142:143]))
    Spare = 0
    assigned_mode = bin_int(pp[146:147])
    RAIM = bin_int(pp[147:148])
    comm_state = bin_int(pp[148:149])
    state_syncstate = bin_int(pp[149:151])
    state_slottimeout = bin_int(pp[151:154])
    state_slotoffset = bin_int(pp[154:168])
    tt = ''
    for i in range(len(ss)):
        tt = tt + ',' + ss[i]

    return [tt, ss[0][0:10],MessageID ,RepeatIndicator ,UserID,Altitude ,SOG ,PositionAccuracy ,Position_longitude ,Position_latitude ,COG ,TimeStamp ,Reserved ,DTE , Spare , assigned_mode ,RAIM ,comm_state ,state_syncstate ,state_slottimeout ,state_slotoffset ]