pyr=[
    [13],
    [11,8],
    [12,7,26],
    [6,14,15,8],
    [12,17,13,24,11]
]
"""
动态分布实现。
"""
arr = []
pre = []
for k in range(4,-1,-1):
    if k == 4:
        arr = pyr[4]
    for i in range(0,k):
        pre.append(max(arr[i],arr[i+1])+pyr[k-1][i])
    print(arr)
    arr = pre[:]
    pre = []




# arr = []
# sum_dict={}
# def pyrma(x,y):
#
#     if x>3:
#         global sum_dict
#         arr.append(pyr[4][y])
#         lis = arr[:]
#         sum_dict.update({sum(arr):lis})
#         #print(arr,sum(arr))
#         arr.pop()
#     else:
#             arr.append(pyr[x][y])
#             for i in range(0,2):
#                 pyrma(x+1,y+i)
#             arr.pop()
# if __name__=='__main__':
    # pyrma(0,0)
    # max_sort = sorted(sum_dict.items(),key=lambda e:e[0],reverse=True)
    # print(max_sort[0])
