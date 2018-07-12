#程式的包裝：把九九乘法表包裝成函數，可做n1xn2乘法
#print("作業1-1：幾幾乘法表")

# n1=input("要幾乘幾的乘法表？")
# n1=int(n1)
# n2=n1

def list(n1,n2):  
    for x in range(1,n1+1):
        for y in range(1,n2+1):
            print(x,"*",y,"=",x*y)

    return

#a=input("要幾乘幾的乘法表？")
#b=input("要幾乘幾的乘法表？")
#a=int(a)
#b=int(b)
#測試後發現，直接輸入數字會被當成str，所以要指定為int
#n1=input("要幾乘幾的乘法表？")
#n2=input("要幾乘幾的乘法表？")
#n1=int(n1)
#n2=n1

