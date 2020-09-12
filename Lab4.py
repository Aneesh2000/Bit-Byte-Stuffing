#Sender Side

def split(word):
    return [char for char in word]


def listToString(s):
    str1 = ""
    for ele in s:
        str1 += ele
    return str1

def ByteStuffing():
    x = input("Enter data to be sent :")
    flag = '@'
    esc = '$'
    list = split(x)
    #print(list)
    i=0
    while(i<len(list)):
        if list[i]==flag or list[i]==esc:
            list.insert(i,esc)
            i+=1
        i+=1

    #print(list)
    list.insert(0,flag)
    list.append(flag)
    x= listToString(list)
    print("Stuffed Data")
    print(x)

    #Receiver Side
    del list[0]
    del list[len(list)-1]

    i=0
    while(i<len(list)):
        if list[i]==esc:
            del list[i]
            i+=1
        i+=1
    i=0
    x = listToString(list)
    print("UnStuffed Data")
    print(x)

def BitStuffing():
    #sender
    y = input("Enter binary data to be sent :")
    list1 = split(y)
    count = 0
    for i in range(len(list1)):
        if list1[i] == '1':
            count = count + 1
        else:
            count = 0
        if count == 5:
            list1.insert(i + 1, '0')

    flag1=['0','1','1','1','1','1','1','0']
    for i in range(0,8):
        list1.insert(0,flag1[i])
        list1.append(flag1[i])
    x = listToString(list1)
    print("Stuffed Data")
    print(x)

    #Receiver
    for i in range(0,8):
        del list1[0]
        list1.pop()
    count = 0
    for i in range(len(list1)-1):
        if list1[i] == '1':
            count = count + 1
        else:
            count = 0
        if count == 5:
            del list1[i + 1]

    x = listToString(list1)
    print("UnStuffed Data")
    print(x)

z = int(input("enter 1 for Byte Stuffing\n2 for bit stuffing :"))
if z==1:
    ByteStuffing()
elif z==2:
    BitStuffing()
else:
    print("please enter a valid input")









    a = int(input("enter 1 for vrc\n 2 for lrc :"))
    b = int(input("enter 1 for even parity\n 2 for odd parity :"))
    if a == 1 and b == 1:
        vrceve()
    elif a == 1 and b == 2:
        vrcodd()
    elif a == 2 and b == 1:
        lrceve()
    elif a == 2 and b == 2:
        lrcodd()
    else:
        print("enter valid input")