# difference from hw1_18.py: use PLA instead of pocket algorithm => MUCH faster, but the error rate is higher (0.131=>0.271)
import random
import numpy as np

NUMBER = 500 #number of rows in the data 
DIM = 4 #dimension of Xn
# 設定實驗次數和數據點數量
num_experiments = 2000
num_data_points = NUMBER
updates = 50
#read train dataset
co=0 #算過，共400筆資料
w=[0]*5 #include w0
data=[]

train_file=open("train_data.txt","r")
test_file=open("test_data.txt","r")

while co < NUMBER:
    tmp=train_file.readline()
    tmp=tmp.split()
    for i in range(len(tmp)):
        tmp[i]=float(tmp[i])
    tmp.insert(0,float(1))
    data.append(tmp)
    co += 1

# read test data
data2 = [] # reset data
co = 0
while co < NUMBER:
    tmp=test_file.readline()
    tmp=tmp.split()
    for i in range(len(tmp)):
        tmp[i]=float(tmp[i])
    tmp.insert(0,float(1))
    data2.append(tmp)
    co += 1

total_err_rate=0
# 進行多次實驗: train/test
for exp in range(num_experiments):
    print(f"exp:{exp}")#test
    min_err = float('Inf')
    # 使用不同的隨機種子
    random_seed = exp  # 使用實驗次數作為隨機種子
    random.seed(random_seed)
    w=[0]*5 #include w0, reset w
    # 生成隨機順序的數據點索引
    data_indices = list(range(NUMBER))
    random.shuffle(data_indices)
    # 在這裡執行你的演算法，使用生成的隨機順序處理數據點: train
    travel_through = 0
    co_updates = 1
    pre_index = NUMBER - 1
    while True:
        cal=0
        for i in range(DIM + 1): # including X0
            cal += w[i] * data[data_indices[travel_through]][i]
        # print(f"sign:{np.sign(cal)} data[travel_through][DIM + 1]:{data[travel_through][DIM + 1]}", end=' ') #test
        if (np.sign(cal) == data[data_indices[travel_through]][DIM + 1]) or (cal == 0 and data[data_indices[travel_through]][DIM + 1] == -1): #tmp[4] is yn
            pass
        else:
            for i in range(DIM + 1):
                w[i] = w[i] + data[data_indices[travel_through]][i] * data[data_indices[travel_through]][DIM + 1] # w(t+1)=w(t) + y(t)x(t)

            co_updates += 1
            if co_updates >= updates:
                # print(f"min_err: {min_err}") # test
                break
        if travel_through == NUMBER - 1:
            travel_through = 0
        else:
            travel_through += 1
    # 在這裡執行你的演算法，使用生成的隨機順序處理數據點: test
    cnt_err = 0
    travel_through = 0
    while travel_through < NUMBER:
        cal = 0
        for i in range(DIM + 1):
            cal += w[i] * data2[data_indices[travel_through]][i]
        if cal == 0: 
            if data2[data_indices[travel_through]][DIM + 1] != -1: #tmp[4] is yn
                cnt_err += 1
        elif  np.sign(cal) != data2[data_indices[travel_through]][DIM + 1]:
            cnt_err += 1

        travel_through += 1
    print(cnt_err / NUMBER)
    total_err_rate += cnt_err / NUMBER

# 在所有實驗結束後，計算平均錯誤率
print(total_err_rate / num_experiments)

# close the file
train_file.close()
test_file.close()