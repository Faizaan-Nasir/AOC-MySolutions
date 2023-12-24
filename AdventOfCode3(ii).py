file=open('assignment1.txt','r') # i've always been criticised for my terrible file/variable naming skills
a=file.readlines()
# we'll be using coordinate system for this particular solution
# to kinda understand what's going on, try printing 'd' at the end
def checknum(k):
    l=[]
    num=''
    for j in k:
        if j.isdigit():
            num+=j
        elif num!='':
            l.append(num)
            num=''
    else:
        if num!='':
            l.append(num)
    return l
d={}
for i in range(0,len(a)):
    li=checknum(a[i])
    for j in li:
        h=a[i].index(j) # a fine example of why i shouldn't be the one naming variables
        if h==0:
            u=0 # this u is gonna be an absolute nightmare in the future but just remeber that we've set this to check if its the first character, coz first characters don't have diagonals on the left
        else:
            u=h-1 # in any other situation they'd have a diagonal on the left and hence u=h-1 has been declared
        k='*'
        # genuinely speaking, the following if statement is completely useless and is only there coz i was lazy
        if k == '*':
            if i==0: # this if block exists to check if we're talking about the very first line, coz if we're then there's no line before the first line and so no upper diagonals to be considered
                if k in a[i][u:h+len(j)+1]: # like i said 'u' is a total nightmare, here it's checking the diagonals in the same line a[i]
                    try:
                        d[(i+1,u+a[i][u:h+len(j)+1].index('*'))].append(int(j)) # this statement appends a new number to the list of numbers of same coordinate if its associated with a coordinate previously created
                    except:
                        d[(i+1,u+a[i][u:h+len(j)+1].index('*'))]=[int(j)] # this statement creats a new list and has exactly one element associated with '*' and key would be the coordinates of the '*'
                    a[i]=a[i][:h]+'a'*len(j)+a[i][h+len(j):] # adding of 'a' was with intent of debugging, for you to see my pains, i've left it as it is
                    continue
                elif k in a[i+1][u:h+len(j)+1]: # here it's checking the diagonals in a line after the current one a[i+1]
                    try:
                        d[(i+2,u+a[i+1][u:h+len(j)+1].index('*'))].append(int(j))
                    except:
                        d[(i+2,u+a[i+1][u:h+len(j)+1].index('*'))]=[int(j)]
                    a[i]=a[i][:h]+'a'*len(j)+a[i][h+len(j):]
                    continue
                else:
                    a[i]=a[i][:h]+'h'*len(j)+a[i][h+len(j):] # just like 'a' was absolutely useless (only for debugging) 'h' infact is also a debugging character, i've left it for you to see my pain
            elif i==len(a)-1: # this elif block exists to check if we're talking about the very last line, coz if we're then there's no line after the last line and so no lower diagonals to be considered
                if k in a[i][u:h+len(j)+1]:
                    try:
                        d[(i+1,u+a[i][u:h+len(j)+1].index('*'))].append(int(j))
                    except:
                        d[(i+1,u+a[i][u:h+len(j)+1].index('*'))]=[int(j)]
                    a[i]=a[i][:h]+'a'*len(j)+a[i][h+len(j):]
                    continue
                elif k in a[i-1][u:h+len(j)+1]: # here it's checking a line before a[i-1] for diagonal as well as elements above
                    try:
                        d[(i,u+a[i-1][u:h+len(j)+1].index('*'))].append(int(j))
                    except:
                        d[(i,u+a[i-1][u:h+len(j)+1].index('*'))]=[int(j)]
                    a[i]=a[i][:h]+'a'*len(j)+a[i][h+len(j):]
                    continue
                else:
                    a[i]=a[i][:h]+'h'*len(j)+a[i][h+len(j):]
            else:
                if k in a[i][u:h+len(j)+1]:
                    try:
                        d[(i+1,u+a[i][u:h+len(j)+1].index('*'))].append(int(j))
                    except:
                        d[(i+1,u+a[i][u:h+len(j)+1].index('*'))]=[int(j)]
                    a[i]=a[i][:h]+'a'*len(j)+a[i][h+len(j):]
                    continue
                elif k in a[i+1][u:(h+len(j)+1)]:
                    try:
                        d[(i+2,u+a[i+1][u:(h+len(j)+1)].index('*'))].append(int(j))
                    except:
                        d[(i+2,u+a[i+1][u:(h+len(j)+1)].index('*'))]=[int(j)]
                    a[i]=a[i][:h]+'a'*len(j)+a[i][h+len(j):]
                    continue
                elif k in a[i-1][u:(h+len(j)+1)]:
                    try:
                        d[(i,u+a[i-1][u:(h+len(j)+1)].index('*'))].append(int(j))
                    except:
                        d[(i,u+a[i-1][u:(h+len(j)+1)].index('*'))]=[int(j)]
                    a[i]=a[i][:h]+'a'*len(j)+a[i][h+len(j):]
                    continue
                else:
                    a[i]=a[i][:h]+'h'*len(j)+a[i][h+len(j):]
# at this point we've gotten all the numbers stored in a list paired with the coordinates of the '*' they are associated with in a dictionary
# the key of the dictionary is the coordinates and the list is the value we're concerned with
prods=[]
for keys in d:
    if len(d[keys])==2:
        # only multiplying those values in lists and appending to another list called prods that have exactly 2 values (1 pair of gear number)
        temp=1
        for num in d[keys]:
            temp*=num
        prods.append(temp)
print('The required sum is:',sum(prods))
file.close()