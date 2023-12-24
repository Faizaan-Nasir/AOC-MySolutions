# seed to soil to fertilizer to water to light to temperature to humidity to location
# destination start, source start, length
with open('assignment1.txt','r') as file:
    lines=file.readlines()
    seeds=lines[0].strip('seeds:').split()
    lines.pop(0)
    i=0
    l=[]
    while i<len(lines):
        try:
            ele=lines[i].split()
            for j in range(len(seeds)):
                if int(ele[1])<=int(seeds[j]) and (int(ele[1])+int(ele[2]))>int(seeds[j]) and j not in l:
                    seeds[j]=(int(ele[0])+int(ele[2]))-(int(ele[1])+int(ele[2])-int(seeds[j]))
                    l.append(j)
        except:
            l=[]
        i+=1
print('minimum seeds: ',min(seeds))