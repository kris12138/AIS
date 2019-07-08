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
    MessageID = 18
    RepeatIndicator = bin_int(pp[6:8])
    UserID = bin_int(pp[8:38])
    Reserved1 = 0
    SOG = bin_int(pp[46:56])
    PositionAccuracy = bin_int(pp[56:57])
    longitude = bin_int(pp[57:85])/600000
    latitude = bin_int(pp[85:112])/ 600000
    COG = bin_int(pp[112:124])
    TrueHeading = bin_int(pp[124:133])
    TimeStamp = bin_int(pp[133:139])
    Reserved2=0
    Spare = 0
    cs_unit = bin_int(pp[147:148])
    display_flag = bin_int(pp[142:143])
    dsc_flag = bin_int(pp[143:144])
    band_flag = bin_int(pp[144:145])
    msg22_flag = bin_int(pp[145:146])
    mode_flag = bin_int(pp[146:147])
    RAIM = bin_int(pp[147:148])
    CommStateSelector = bin_int(pp[148:149])
    CommState = bin_int(pp[149:168])
    tt = ''
    for i in range(len(ss)):
        tt = tt + ',' + ss[i]

    return [tt, ss[0][0:10],MessageID,RepeatIndicator ,UserID ,Reserved1 ,SOG ,PositionAccuracy ,longitude ,latitude,COG ,TrueHeading ,TimeStamp ,Spare ,cs_unit ,display_flag ,dsc_flag ,band_flag,msg22_flag,mode_flag ,RAIM,CommStateSelector ,CommState ]