values = [
    [0, 20, 50, 65, 80, 85, 85],
    [0, 20, 40, 50, 55, 60, 65],
    [0, 25, 60, 85, 100, 110, 115],
    [0, 25, 40, 50, 60, 65, 70]
]

#假设老三能支配的投资金额为10*i万元，其中j*10万投给老四，其中i在(1,7)之间
#加载i为1~6时的最大回报率，则能统计出当老三拥有10*i万时最大的投资回报额list。
pre_max = values[3]
for k in range(3,-1,-1):
    new_pre = [0]
    for i in range(1,7):
        arr = []
        for j in range(0,i+1):
            arr.append(pre_max[j]+values[k-1][i-j])
        new_pre.append(max(arr))
    pre_max = new_pre

print(pre_max)

