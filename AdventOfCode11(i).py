with open('assignment1.txt','r') as file:
    data=file.readlines()
    a=1
    d={}
    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j]=='#':
                d[a]=[data[i].index(data[i][j])+1,data.index(data[i])+1]
                data[i]=data[i][:j]+'*'+data[i][j+1:]
                a+=1
    print(d)
    xcoordinates=[i[0] for i in d.values()]
    ycoordinates=[i[1] for i in d.values()]
    tempdy={}
    for i in d:
        tempdy[i]=0
    for i in range(1,len(data)+1):
        if i not in ycoordinates:
            for j in d:
                if d[j][1]>i:
                   tempdy[j]+=1
    for i in d:
        for j in tempdy:
            if i==j:
                d[i][1]+=tempdy[j]
    tempdx={}
    for i in d:
        tempdx[i]=0
    for i in range(1,len(data[0].strip('\n'))+1):
        if i not in xcoordinates:
            for j in d:
                if d[j][0]>i:
                    tempdx[j]+=1
    for i in d:
        for j in tempdx:
            if i==j:
                d[i][0]+=tempdx[j]
    print(d)
    comb=[]
    for i in d.keys():
        for j in d.keys():
            if (i,j) not in comb and i!=j and (j,i) not in comb:
                comb.append((i,j))
    dist=0
    for i in comb:
        k=dist
        dist+=abs(d[i[0]][0]-d[i[1]][0])+abs(d[i[0]][1]-d[i[1]][1])
    print(dist)