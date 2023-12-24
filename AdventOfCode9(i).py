with open('assignment1.txt','r') as file:
    data=file.readlines()
    s=0
    for i in data:
        line=i.split()
        differences=[]
        count=0
        storingvar=[list(map(lambda x: int(x),line))]
        while True:
            for j in range(len(line)):
                try:
                    differences.append(int(line[j+1])-int(line[j]))
                except:
                    pass
            zerocount=differences.count(0)
            storingvar.append(differences)
            count+=1
            if zerocount==len(differences):
                break
            else:
                line=differences.copy()
                differences=[]
        storingvar[-1].append(0)
        for index in range(2,len(storingvar)+1):
            storingvar[-index].append(storingvar[-index][-1]+storingvar[-index+1][-1])
        s+=storingvar[0][-1]
    print(s)