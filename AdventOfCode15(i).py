with open('assignment1.txt','r') as file:
    data=file.read().split(',')
    s=0
    for i in data:
        thisnum=0
        for j in i:
            thisnum+=ord(j)
            thisnum*=17
            thisnum%=256
        s+=thisnum
    print(s)