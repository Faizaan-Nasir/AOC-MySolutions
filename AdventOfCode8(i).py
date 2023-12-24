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
    position='AAA'
    count=0
    while position!='ZZZ':
        for i in instructions:
            if i=='L':
                position=infodict[position][0]
            else:
                position=infodict[position][1]
            count+=1
            if position=='ZZZ':
                break
    print(count)