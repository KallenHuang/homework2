#使用者輸入一個數字，算出整數平方根
print("作業2")
n=int(input("輸入一個正整數："))
k=0
if n>0:
    while n:
#        print(k,n)
        k+=1
        if k*k<n:
#            print("k的平方為",k*k)
            continue
        elif k*k==n:
            print("此數的整數平方根為：",k)
            break
        else:
            print("此數無整數平方根")
            break
else:
    print("不輸入正整數無法執行")