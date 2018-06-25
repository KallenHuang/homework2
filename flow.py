#流程控制
#if 布林值:
#    如果布林值是 Ture 執行這個程式區塊 #前面需要縮排，必要時眼睛要看不能依賴編輯器
#if True:
#    print("Hello")
money=int(input("多少錢?"))
if money<=30000:
    print("OK")
else:
    #如果布林值是False，執行這個區塊
    print("Too Much")

money1=int(input("多少錢?"))
if money1<=0:
    print("請輸入大於0的數字")
elif money1<=30000:
    print("OK")
elif money1<=40000:
    print("OK1")
else:
    print("Too Much")

# n1=int(input("Enter a Number:"))
# n2=int(input("Enter a Number:"))
# op=input("運算：+,-,*,/")

#中央處理器 CPU 1GHz
#10億個指令/每秒

#迴圈
#while 布林值: if是跑完就結束了，while跑完還會再跑
    #如果布林值是Ture，執行這個區塊的程式碼
n=1
while n<=5:
    print(n)
    n+=1
print("Final",n)
#break和continue都是用在迴圈裡面才有意義，在外面是沒有意義的
n=1
while n<=5:
    print(n)
    n+=1
    if n==3:
        break #立即終止迴圈
print("Final",n)


x=1
while x<=5:
    x+=1
    if x==3:
        continue #立刻進入倒下一個迴圈
    print(x)
print("Final",x)

x=1
while x<=5:
    x+=1
    if x%2==0:#如果n是偶數
        continue #立刻進入倒下一個迴圈
    print(x)
print("Final",x)

#1+2+....+50
#result=(1+50)*50/2

sum=0 #記錄最後總加的結果
k=1 #在迴圈中追蹤1,2,3,....,50
while k<=50:
    print(k,sum) #簡化問題並且把訊息印出來，是了解問題的方法
    sum=sum+k #將n的數字累加進sum裡面
    k+=1 #加1之後再加上之前的數字
print(sum)

# n=int(input("輸入一個起始的正整數"))
# k=1
# while k*k<=n:
#     print(k,n)
#   k=


#for變數名稱in列表：
#   迴圈區塊
for n in [2,5,6,7]:
    print(n)
print("======")

for r in range(1,6): #range(1,6)產生[1,2,3,4,5]的列表
    print(r)




#a=int(input("輸入一個起始的正整數"))
#b=int(input("輸入一個最終的正整數"))
# while a<=b:
#     a+=1
#     if a+1<b

# print("第一個數字",x1,"累加到",x2,"的總和為：")