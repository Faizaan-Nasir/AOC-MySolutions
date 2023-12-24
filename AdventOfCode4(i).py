with open ('assignment1.txt','r') as file:
    lines=file.readlines()
    suml=[]
    for i in lines:
        locatecol=i.index(':')
        actualline=i[locatecol+1:]
        tupwin=actualline.partition('|')
        winnum=tupwin[0].split()
        cardnums=tupwin[2].split()
        latestnum=0
        for j in cardnums:
            if j in winnum:
                if latestnum==0:
                    latestnum=1
                else:
                    latestnum*=2
        suml.append(latestnum)
    print(sum(suml))
        