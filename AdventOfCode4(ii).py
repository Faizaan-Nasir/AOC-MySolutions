'''Here's the deal, this one works and works always.
But this code took me a whole day to develop.
Looks short and, thanks to my variable naming skills, it is confusing, but trust me when I say this, this wasn't my algorithm initially.
For day 3, I provided a brief of each statement, I havent done so here, it's not worth explaining'''

with open ('assignment1.txt','r') as file:
    lines=file.readlines()
    newl={}
    count={}
    for i in lines:
        locatecol=i.index(':')
        actualline=i[locatecol+1:]
        tupwin=actualline.partition('|')
        winnum=tupwin[0].split()
        cardnums=tupwin[2].split()
        newl[i[:locatecol].replace(' ','')]=(winnum,cardnums)
        count[i[:locatecol].replace(' ','')]=1
    newlcopy=newl.copy()
    j=0
    while j < len(newlcopy):
        keys=list(newlcopy.keys())        
        for h in range(count[keys[j]]):
            arandomnum=1
            for k in newlcopy[keys[j]][0]:
                if k in newlcopy[keys[j]][1]:
                    num=''
                    for q in keys[j]:
                        if q.isdigit():
                            num+=q
                    a=int(num)+arandomnum
                    string='Card'+str(a)
                    count[string]+=1
                    arandomnum+=1
        j+=1
    s=0
    print(count)
    for m in count:
        s+=count[m]
    print(s)