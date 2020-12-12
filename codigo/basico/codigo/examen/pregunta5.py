



for i in range(5):
    print(i)




    lis = [x * x for x in range(5)]

def fun(lis):
    del lis[lis[2]]
    return lis

print(fun(lis))