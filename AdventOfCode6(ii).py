with open('assignment1.txt','r') as file:
    data=file.readlines()
    time=''.join(data[0].strip('Time:').split())
    distance=''.join(data[1].strip('Distance:').split())
    print(time,distance)
    for hold in range(0,int(time)):
        speed=hold
        remaintime=int(time)-hold
        disttravelled=remaintime*speed
        if disttravelled>int(distance):
            lower=hold
            break
    for revhold in range(int(time),0,-1):
        speed=revhold
        remaintime=int(time)-revhold
        disttravelled=remaintime*speed
        if disttravelled>int(distance):
            upper=revhold
            break
    print(upper,lower)
    print(upper+1-lower)