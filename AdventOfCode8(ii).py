import math
with open('assignment1.txt','r') as file:
    data=file.readlines()
    instructions=data.pop(0).strip('\n')
    infodict={}
    for line in data:
        datatup=line.split('=')
        within=datatup[1].split(',')
        datatup[0]=datatup[0].strip()
        within[0]=within[0].strip(' (')
        within[1]=within[1].strip(' )\n')
        infodict[datatup[0]]=within
    positionlis=[i for i in infodict if i[-1]=='A']
    count=[]
    for position in positionlis:
        counter=0
        while position[-1]!='Z':
            for i in instructions:
                if i=='L':
                    position=infodict[position][0]
                else:
                    position=infodict[position][1]
                counter+=1
                if position[-1]=='Z':
                    break
        count.append(counter)
    lcm=math.lcm(*count)
    print(lcm)