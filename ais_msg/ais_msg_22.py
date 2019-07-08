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
    MessageID = 22
    RepeatIndicator = bin_int(pp[6:8])
    UserID = bin_int(pp[8:38])
    Spare = 0
    ChanA = bin_int(pp[40:52])
    ChanB = bin_int(pp[52:64])
    TxRxMode = bin_int(pp[64:68])
    power = bin_int(pp[68:69])
    corner1_lon = bin_int(pp[69:87])
    corner1_lat = bin_int(pp[87:104])
    corner2_lon = bin_int(pp[104:122])
    corner2_lat = bin_int(pp[122:139])
    IndicatorType = bin_int(pp[139:140])
    ChanABandwidth = bin_int(pp[140:141])
    ChanBBandwidth = bin_int(pp[141:142])
    TransZoneSize = bin_int(pp[142:145])
    Spare2 = 0
    tt = ''
    for i in range(len(ss)):
        tt = tt + ',' + ss[i]

    return [tt, ss[0][0:10],MessageID ,RepeatIndicator ,UserID , Spare ,ChanA ,ChanB ,TxRxMode ,power ,corner1_lon ,corner1_lat ,corner2_lon ,corner2_lat ,IndicatorType ,ChanABandwidth ,ChanBBandwidth ,TransZoneSize ,Spare2 ]