import numpy as np

NUMBER = 400 #number of rows in the data 
DIM = 4 #dimension of Xn

co=0 #算過，共400筆資料
w=[0]*5 #include w0
data=[]

while co < NUMBER:
    tmp=input()
    tmp=tmp.split()
    for i in range(len(tmp)):
        tmp[i]=float(tmp[i])
    tmp.insert(0,float(1))
    data.append(tmp)
    co += 1

# mistakes=0
travel_through = 0
co_updates = 1
pre_index=-1
while True:
    cal=0
    for i in range(DIM + 1): # including X0
        cal += w[i] * data[travel_through][i]
    # print(f"sign:{np.sign(cal)} data[travel_through][DIM + 1]:{data[travel_through][DIM + 1]}", end=' ') #test
    if np.sign(cal) == data[travel_through][DIM + 1]: #tmp[4] is yn
        if travel_through == pre_index:
            print(f"co_updates: {co_updates}")
            break
        if travel_through == NUMBER - 1:
            travel_through = 0
        else:
            travel_through += 1
        # print(f"travel:{travel_through}") #test
    else:
        for i in range(DIM + 1):
            w[i] = w[i] + data[travel_through][i] * data[travel_through][DIM + 1] # w(t+1)=w(t) + y(t)x(t)
        co_updates += 1
        if travel_through == 0:
            travel_through = 1
            pre_index = -1 #here改(NUMBER - 1) ?!
        elif travel_through == NUMBER - 1:
            pre_index = travel_through - 1
            travel_through = 0
        else:
            pre_index = travel_through - 1
            travel_through += 1
        # print(f"travel:{travel_through}") #test
        continue
