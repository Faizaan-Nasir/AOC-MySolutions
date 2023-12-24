file=open('assignment1.txt','r')
a=file.readlines()
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
s=0
q=[]
for i in range(0,len(a)):
    li=checknum(a[i])
    for j in li:
        h=a[i].index(j)
        if h==0:
            u=0
        else:
            u=h-1
        for k in '*#%=-/+$@&':
            if i==0:
                if k in a[i][u:h+len(j)+1]:
                    q.append(int(j))
                    a[i]=a[i][:h]+'a'*len(j)+a[i][h+len(j):]
                    break
                elif k in a[i+1][u:h+len(j)+1]:
                    q.append(int(j))
                    a[i]=a[i][:h]+'a'*len(j)+a[i][h+len(j):]
                    break
                else:
                    a[i]=a[i][:h]+'h'*len(j)+a[i][h+len(j):]
            elif i==len(a)-1:
                if k in a[i][u:h+len(j)+1]:
                    q.append(int(j))
                    a[i]=a[i][:h]+'a'*len(j)+a[i][h+len(j):]
                    break
                elif k in a[i-1][u:h+len(j)+1]:
                    q.append(int(j))
                    a[i]=a[i][:h]+'a'*len(j)+a[i][h+len(j):]
                    break
                else:
                    a[i]=a[i][:h]+'h'*len(j)+a[i][h+len(j):]
            else:
                if k in a[i][u:h+len(j)+1]:
                    q.append(int(j))
                    a[i]=a[i][:h]+'a'*len(j)+a[i][h+len(j):]
                    break
                elif k in a[i+1][u:(h+len(j)+1)]:
                    q.append(int(j))
                    a[i]=a[i][:h]+'a'*len(j)+a[i][h+len(j):]
                    break
                elif k in a[i-1][u:(h+len(j)+1)]:
                    q.append(int(j))
                    a[i]=a[i][:h]+'a'*len(j)+a[i][h+len(j):]
                    break
                else:
                    a[i]=a[i][:h]+'h'*len(j)+a[i][h+len(j):]
print(sum(q))
file.close()