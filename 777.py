"""
求n个数字相加，总和为7的所有可能
"""
arr=[]
def infor(n):
    global total
    if n==0:
        total+=1
        print(arr)
    else:
        for i in range(1,n+1):
            next_n = n-i
            arr.append(i)
            infor(next_n)
            arr.remove(i)

if __name__=="__main__":
    total=0
    infor(7)
    print(total)
