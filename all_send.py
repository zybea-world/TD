"""
具体分析为:
设置现场：
老大depth=1，从剩余的数字列表datas中随机选择一个数字加空列表中，即arr.append(data)
next_datas = datas[:] 每一个for循环中不要直接去改变datas的值
name剩余的可选数字列表就是next_datas.remove(data)
然后递归：
search(depth+1,next_datas)
恢复现场：
arr.pop(),递归后，将arr恢复，放入另一个数字，继续传递给depth+1
注意
当depth达到最大值后输出，且也需要将刚才传入的值去掉然后恢复，开始下一轮传递，arr.pop()
"""
def search(depth,datas):
    global total
    if depth==4:
        arr.append(datas[0])
        print(arr)
        total+=1
        arr.pop()
    else:
        for data in datas:
            arr.append(data)
            next_datas = datas[:]
            next_datas.remove(data)
            search(depth+1,next_datas)
            arr.pop()

if __name__=="__main__":
    list = [1, 2, 3, 4]
    arr = []
    total = 0
    search(1,list)
    print(total)




