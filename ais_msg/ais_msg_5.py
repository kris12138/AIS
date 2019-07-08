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
    MessageID = 5
    RepeatIndicator = bin_int(pp[6:8])
    UserID = bin_int(pp[8:38])
    AISversion = bin_int(pp[38:40])
    IMOnumber = bin_int(pp[40:70])
    callsign = bin_int(pp[70:112])
    name = bin_int(pp[112:232])
    shipandcargo = bin_int(pp[232:240])
    dimA = bin_int(pp[240:249])
    dimB = bin_int(pp[249:258])
    dimC = bin_int(pp[258:264])
    dimD = bin_int(pp[264:270])
    fixtype = bin_int(pp[270:274])
    ETAmonth = bin_int(pp[274:278])
    ETAday = bin_int(pp[278:283])
    ETAhour = bin_int(pp[283:288])
    ETAminute = bin_int(pp[288:294])
    draught = bin_int(pp[294:302])
    destination = bin_int(pp[302:422])
    dte = bin_int(pp[422:423])
    Spare =0
    tt = ''
    for i in range(len(ss)):
        tt = tt + ',' + ss[i]

    return [tt, ss[0][0:10],MessageID , RepeatIndicator ,UserID ,AISversion ,IMOnumber ,callsign , name , shipandcargo ,dimA ,dimB , dimC , dimD, fixtype ,ETAmonth ,ETAday ,ETAhour , ETAminute ,draught ,destination , dte , Spare ]