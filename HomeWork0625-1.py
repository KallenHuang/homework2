#作業1：作業1：輸入兩個數字，然後請使用者輸入加減乘除，就要幫使用者對這兩個數字加減乘除
print("====================")
print("作業1：")

n1=int(input("Enter a Number:"))
n2=int(input("Enter a Number:"))
op=input("輸入運算符號：+,-,*,/：")

if op=="+":
    print(n1,"加",n2,"等於",n1+n2)
elif op=="-":
    print(n1,"減",n2,"等於",n1-n2)
elif op=="*":
    print(n1,"乘",n2,"等於",n1*n2)
elif op=="/":
    print(n1,"除",n2,"等於",n1/n2)
else:
    print("輸入錯誤就不幫你算喔～")

print("====================")

#作業2：使用者輸入一個數字，算出整數平方根
print("作業2：")
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

print("====================")


#作業3：用迴圈的方式寫兩層，印出99乘法表。(建議用for迴圈做)
print("作業3：九九乘法表")

for x in range(1,10):
    for y in range(1,10):
#        print(x,y)
         print(x,"*",y,"=",x*y)


print("====================")