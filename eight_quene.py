"""
回溯法适用于穷举所有的可能性
先理清楚第一个步骤到第二个步骤的关系，知道最后一个步骤后达到条件输出
一般的参数传递为步骤数，和解空间
比如八皇后问题，步骤数就是第几行，而解空间就是8个皇后
而 列举1,2,3的所有排列方式，步骤数是第几步，解空间就是剩余可选的数字
一本格式为：

def search(step,datas):
    if step == max:
        do_sth
        #考虑时候恢复
        pass
    else:
        for i in range(datas):
            设置现场
            递归
            恢复现场
"""





import numpy as np
board = np.random.randint(0,1,(8,8)).tolist()

def can_place(x,y):

    #判断x行是否有皇后：
    for i in range(0,y):
        if board[x][i]==1:
            return False
    #判断y列是否有皇后：
    for i in range(x):
        if board[i][y] == 1:
            return False
    #判断‘/’是否有皇后：
    for  i in range(x):
        if  x+y-i<=7 and board[i][x+y-i]==1:
            return False
    #判断 ‘\’是否有皇后
    for index,i in enumerate(range(x-1,-1,-1)):
        if y-index-1>= 0 and board[i][y-index-1] == 1:
            return False
    return True

def print_board():
    for i in range(8):
        for j in range(8):
            if board[i][j]==1:
                print("■ ",end=" ")
            else:
                print("□ ",end=" ")
        print()

total = 0
def put_queue(step):
    global total
    if step == 8:
        print_board()
        total+=1
        print('-------------------------------------------------')
    else:
        for i in range(8):
            if can_place(step,i):#判断能否移动皇后
                #设置现场
                #判断为True时，将该点设置为1
                board[step][i]=1
                #然后开始递归
                put_queue(step+1)
                #递归结束后，将现场恢复
                board[step][i]=0


if __name__=='__main__':
    put_queue(0)
    print(total)







