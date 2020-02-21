info = [
    [3, 8],
    [2, 5],
    [5, 12]
]
total = 5
arr=[]
dict = []
max=0
def search(depth,rest):
    #当到了第三个人做决议的时候
    #使用
    if depth==3:
        global max, arr
        max_value = 0
        dict = arr[:]
        for index,i in enumerate(dict):
            max_value += info[index][1]*i
        if max <= max_value:
            max = max_value
        print(max,dict)

    else:
        arr.append(0)
        search(depth + 1, rest)
        arr.pop()
        if rest >= info[depth][0]:
            arr.append(1)
            search(depth+1,rest-info[depth][0])
            arr.pop()
search(0,5)