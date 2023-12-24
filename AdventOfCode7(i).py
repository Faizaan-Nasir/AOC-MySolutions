def orderit(orderwhat):
    while True:
        shudcontinue='no'
        for i in range(len(orderwhat)-1):
            for j in range(5):
                if order.index(orderwhat[i][j])<order.index(orderwhat[i+1][j]):
                    orderwhat[i],orderwhat[i+1]=orderwhat[i+1],orderwhat[i]
                    shudcontinue='yes'
                    break
                elif orderwhat[i][j]==orderwhat[i+1][j]:
                    pass
                else:
                    break
            if shudcontinue=='yes':
                break
            else:
                pass
        else:
            break
    return orderwhat
with open('assignment1.txt','r') as file:
    order=['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']
    data=file.readlines()
    diction={}
    for i in data:
        temp=i.split()
        diction[temp[0]]=temp[1]
    groupeddict={}
    for j in diction.keys():
        currentnum=0
        numberoftwos=0
        for k in j:
            if j.count(k)==5:
                groupeddict[j]='fiveofkind'
                currentnum=j.count(k)
            elif j.count(k)==4 and j.count(k)>currentnum:
                groupeddict[j]='fourofkind'
                currentnum=j.count(k)
            elif j.count(k)==3 and j.count(k)>currentnum:
                if len(set(j))==3:
                    groupeddict[j]='threeofkind'
                elif len(set(j))==2:
                    groupeddict[j]='fullhouse'
                currentnum=j.count(k)
            elif j.count(k)==2 and j.count(k)>=currentnum:
                numberoftwos+=1
                if numberoftwos>2:
                    groupeddict[j]='twopair'
                else:
                    groupeddict[j]='onepair'
                currentnum=j.count(k)
        else:
            try:
                groupeddict[j]
            except:
                groupeddict[j]='highcard'
    highcard=[]
    onepair=[]
    twopair=[]
    fourofkind=[]
    fiveofkind=[]
    threeofkind=[]
    fullhouse=[]
    for keys in groupeddict:
        if groupeddict[keys]=='highcard':
            highcard.append(keys)
        elif groupeddict[keys]=='onepair':
            onepair.append(keys)
        elif groupeddict[keys]=='twopair':
            twopair.append(keys)
        elif groupeddict[keys]=='threeofkind':
            threeofkind.append(keys)
        elif groupeddict[keys]=='fourofkind':
            fourofkind.append(keys)
        elif groupeddict[keys]=='fiveofkind':
            fiveofkind.append(keys)
        elif groupeddict[keys]=='fullhouse':
            fullhouse.append(keys)
    if len(highcard)>1:
        highcard=orderit(highcard)
    if len(onepair)>1:
        onepair=orderit(onepair)
    if len(twopair)>1:
        twopair=orderit(twopair)
    if len(threeofkind)>1:
        threeofkind=orderit(threeofkind)
    if len(fourofkind)>1:
        fourofkind=orderit(fourofkind)
    if len(fiveofkind)>1:
        fiveofkind=orderit(fiveofkind)
    if len(fullhouse)>1:
        fullhouse=orderit(fullhouse)
    final=highcard+onepair+twopair+threeofkind+fullhouse+fourofkind+fiveofkind
    s=0
    for i in range(len(final)):
        s+=int(diction[final[i]])*(i+1)
    print(len(final))
    print(final)
    print(s)