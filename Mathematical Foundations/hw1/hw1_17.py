import random
import numpy as np

NUMBER = 400 #number of rows in the data 
DIM = 4 #dimension of Xn
# 設定實驗次數和數據點數量
num_experiments = 2000
num_data_points = NUMBER
learning_rate = 1
#input dataset
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

total_updates=0  
# 進行多次實驗
for exp in range(num_experiments):
    print(f"exp:{exp}")#test
    # 使用不同的隨機種子
    random_seed = exp  # 使用實驗次數作為隨機種子
    random.seed(random_seed)
    w=[0]*5 #include w0, reset w
    # 生成隨機順序的數據點索引
    data_indices = list(range(num_data_points))
    random.shuffle(data_indices)
    # 在這裡執行你的演算法，使用生成的隨機順序處理數據點
    travel_through = 0
    co_updates = 1
    pre_index = NUMBER - 1
    while True:
        cal=0
        for i in range(DIM + 1): # including X0
            cal += w[i] * data[data_indices[travel_through]][i]
        # print(f"sign:{np.sign(cal)} data[travel_through][DIM + 1]:{data[travel_through][DIM + 1]}", end=' ') #test
        if (np.sign(cal) == data[data_indices[travel_through]][DIM + 1]) or (cal == 0 and data[data_indices[travel_through]][DIM + 1] == -1): #tmp[4] is yn
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
                w[i] = w[i] + learning_rate * data[data_indices[travel_through]][i] * data[data_indices[travel_through]][DIM + 1] # w(t+1)=w(t) + y(t)x(t)
            #為甚麼learning rate改了還是一樣QQ
            co_updates += 1
            if travel_through == 0:
                travel_through = 1
                pre_index = NUMBER - 1
            elif travel_through == NUMBER - 1:
                pre_index = travel_through - 1
                travel_through = 0
            else:
                pre_index = travel_through - 1
                travel_through += 1
            # print(f"travel:{travel_through}") #test
            continue
    # 記錄算法的更新次數
    total_updates += co_updates
# 在所有實驗結束後，計算平均更新次數
print(total_updates / NUMBER)
