#汉诺塔
def move(index,start,mid,end):
    if index == 1:
        print("{}->{}->{}".format(start,index,end))

    else:
        move(index-1,start,end,mid)
        print("{}->{}->{}".format(start,index,end))
        move(index-1,mid,start,end)

if __name__=="__main__":
    move(2,'A','B','C')

