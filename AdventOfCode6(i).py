with open('assignment1.txt','r') as file:
    data=file.readlines()
    time=data[0].strip('Time:').split()
    distance=data[1].strip('Distance:').split()
    chances=[]
    for i in range(len(time)):
        numberoftimes=0
        for hold in range(int(time[i])+1):
            speed=hold
            remaintime=int(time[i])-hold
            disttravelled=remaintime*speed
            if disttravelled>int(distance[i]):
                numberoftimes+=1
        chances.append(numberoftimes)
    result=1
    for j in chances:
        result*=j
    print(result)

        