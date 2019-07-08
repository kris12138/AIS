# from ascii_table import ascii
# from ais_msg import ais_msg_1
# from ais_msg import ais_msg_2
# from ais_msg import ais_msg_3
# from ais_msg import ais_msg_4
# from ais_msg import ais_msg_5
# from ais_msg import ais_msg_6
# from ais_msg import ais_msg_7
# from ais_msg import ais_msg_8
# from ais_msg import ais_msg_9
# from ais_msg import ais_msg_10
# from ais_msg import ais_msg_11
# from ais_msg import ais_msg_12
# from ais_msg import ais_msg_13
# from ais_msg import ais_msg_14
# from ais_msg import ais_msg_15
# from ais_msg import ais_msg_16
# from ais_msg import ais_msg_17
# from ais_msg import ais_msg_18
# from ais_msg import ais_msg_19
# from ais_msg import ais_msg_20
# from ais_msg import ais_msg_21
# from ais_msg import ais_msg_22
#
# import sqlite3
# import time
# import math
# cx = sqlite3.connect("f:/zhoushan_detail.db")
# cu = cx.cursor()
# cx1 = sqlite3.connect("f:/zhoushan.db")
# cu1 = cx1.cursor()
#
#
# def bin_int(tt):
#     sum=0
#     for i in range(len(tt)):
#         sum+=int(tt[i])*(2**(len(tt)-1-i))
#     return sum
# def get_MessageID(ss):
#     pp = ''
#     for j in range(len(ascii)):
#         if ss[0] == ascii[j][1]:
#             pp += ascii[j][2].replace('0b', '')
#     return bin_int(pp[0:6])
# data=[]
# count=10
# with open('data/2018080200.txt','r') as f:
#     for i in f:
#         if(count):
#             count=count-1
#             if(len(i)!=1):
#                 data.append(i.replace('\n','').split(','))
# print(data)
# ais_data=[]
# # for i in range(len(data)):
# for i in range(10):
#     try:
#         MessageID=get_MessageID(data[i][6])
#         if MessageID==1:
#             ais_data.append(ais_msg_1.invert(data[i]))
#         elif MessageID==2:
#             ais_data.append(ais_msg_2.invert(data[i]))
#         elif MessageID==3:
#             ais_data.append(ais_msg_3.invert(data[i]))
#         elif MessageID==4:
#             ais_data.append(ais_msg_4.invert(data[i]))
#         elif MessageID==5:
#             ais_data.append(ais_msg_5.invert(data[i]))
#         elif MessageID==6:
#             ais_data.append(ais_msg_6.invert(data[i]))
#         elif MessageID==7:
#             ais_data.append(ais_msg_7.invert(data[i]))
#         elif MessageID==8:
#             ais_data.append(ais_msg_8.invert(data[i]))
#         elif MessageID==9:
#             ais_data.append(ais_msg_9.invert(data[i]))
#         elif MessageID==10:
#             ais_data.append(ais_msg_10.invert(data[i]))
#         elif MessageID==11:
#             ais_data.append(ais_msg_11.invert(data[i]))
#         elif MessageID==12:
#             ais_data.append(ais_msg_12.invert(data[i]))
#         elif MessageID==13:
#             ais_data.append(ais_msg_13.invert(data[i]))
#         elif MessageID==14:
#             ais_data.append(ais_msg_14.invert(data[i]))
#         elif MessageID==15:
#             ais_data.append(ais_msg_15.invert(data[i]))
#         elif MessageID==16:
#             ais_data.append(ais_msg_16.invert(data[i]))
#         elif MessageID==17:
#             ais_data.append(ais_msg_17.invert(data[i]))
#         elif MessageID==18:
#             ais_data.append(ais_msg_18.invert(data[i]))
#         elif MessageID==19:
#             ais_data.append(ais_msg_19.invert(data[i]))
#         elif MessageID==20:
#             ais_data.append(ais_msg_20.invert(data[i]))
#         elif MessageID==21:
#             ais_data.append(ais_msg_21.invert(data[i]))
#         elif MessageID==22:
#             ais_data.append(ais_msg_22.invert(data[i]))
#     except:
#         pass
#
#
#



import sqlite3
import time
import math
cx = sqlite3.connect("E:/AIS/data/2018080202.db")
cu = cx.cursor()
from ascii_table import ascii
from ais_msg import ais_msg_1
from ais_msg import ais_msg_2
from ais_msg import ais_msg_3
from ais_msg import ais_msg_4
from ais_msg import ais_msg_5
from ais_msg import ais_msg_6
from ais_msg import ais_msg_7
from ais_msg import ais_msg_8
from ais_msg import ais_msg_9
from ais_msg import ais_msg_10
from ais_msg import ais_msg_11
from ais_msg import ais_msg_12
from ais_msg import ais_msg_13
from ais_msg import ais_msg_14
from ais_msg import ais_msg_15
from ais_msg import ais_msg_16
from ais_msg import ais_msg_17
from ais_msg import ais_msg_18
from ais_msg import ais_msg_19
from ais_msg import ais_msg_20
from ais_msg import ais_msg_21
from ais_msg import ais_msg_22
import time
print(time.time())

def bin_int(tt):
    sum=0
    for i in range(len(tt)):
        sum+=int(tt[i])*(2**(len(tt)-1-i))
    return sum
def get_MessageID(ss):
    pp = ''
    for j in range(len(ascii)):
        if ss[0] == ascii[j][1]:
            pp += ascii[j][2].replace('0b', '')
    return bin_int(pp[0:6])
data1=[]


with open('data/2018080202.txt','r') as f:
    for i in f:
        if(len(i)!=1):
            data1.append(i.replace('\n','').split(','))

data=[]
for i in range(len(data1)):
    if(data1[i][2]=='2')&(data1[i][3]=='1'):
        data1[i][6]=data1[i][6]+data1[i+1][6]
        data.append(data1[i])
    elif(data1[i][2]=='2')&(data1[i][3]=='2'):
        pass
    elif (data1[i][2] == '1') & (data1[i][3] == '1'):
        data.append(data1[i])

error_data=[]
ais_data=[]


for i in range(len(data)):
    try:
        MessageID=get_MessageID(data[i][6])
        # print(MessageID)
        if MessageID==1:
            ais_data.append(ais_msg_1.invert(data[i]))
        elif MessageID==2:
            ais_data.append(ais_msg_2.invert(data[i]))
        elif MessageID==3:
            ais_data.append(ais_msg_3.invert(data[i]))
        elif MessageID==4:
            ais_data.append(ais_msg_4.invert(data[i]))
        elif MessageID==5:
            ais_data.append(ais_msg_5.invert(data[i]))
        elif MessageID==6:
            ais_data.append(ais_msg_6.invert(data[i]))
        elif MessageID==7:
            ais_data.append(ais_msg_7.invert(data[i]))
        elif MessageID==8:
            ais_data.append(ais_msg_8.invert(data[i]))
        elif MessageID==9:
            ais_data.append(ais_msg_9.invert(data[i]))
        elif MessageID==10:
            ais_data.append(ais_msg_10.invert(data[i]))
        elif MessageID==11:
            ais_data.append(ais_msg_11.invert(data[i]))
        elif MessageID==12:
            ais_data.append(ais_msg_12.invert(data[i]))
        elif MessageID==13:
            ais_data.append(ais_msg_13.invert(data[i]))
        elif MessageID==14:
            ais_data.append(ais_msg_14.invert(data[i]))
        elif MessageID==15:
            ais_data.append(ais_msg_15.invert(data[i]))
        elif MessageID==16:
            ais_data.append(ais_msg_16.invert(data[i]))
        elif MessageID==17:
            ais_data.append(ais_msg_17.invert(data[i]))
        elif MessageID==18:
            ais_data.append(ais_msg_18.invert(data[i]))
        elif MessageID==19:
            ais_data.append(ais_msg_19.invert(data[i]))
        elif MessageID==20:
            ais_data.append(ais_msg_20.invert(data[i]))
        elif MessageID==21:
            ais_data.append(ais_msg_21.invert(data[i]))
        elif MessageID==22:
            ais_data.append(ais_msg_22.invert(data[i]))
        else:
            error_data.append(data[i])
    except:
        pass
with open('data/message2018080202.csv','w') as f:
    for i in range(len(ais_data)):
        # print(ais_data[i])
        for j in range(len(ais_data[i])):
            f.write(str(ais_data[i][j])+',')
        f.write('\n')

        for j in range(1, 23):

            if (str(ais_data[i][2]) == str(j)):
                b = "INSERT INTO message" + str(j) + " VALUES ('"
                for j in range(len(ais_data[i])):
                    b = b + str(ais_data[i][j]) + "','"
                b = b[0:-2] + ');'
                # print(b)
                m = cu.execute(b)
                break
            else:
                continue
cx.commit()
print('yyyyendddd')

print(time.time())



