
print("作業1-1：幾幾乘法表")

n1=input("要幾乘幾的乘法表？")
n1=int(n1)
n2=n1
import HomeWork0709.HW0709 as h
h.list(n1,n2)

print("作業1-2：四則運算")


n1=int(input("Enter a Number:"))
n2=int(input("Enter a Number:"))
op=input("輸入運算符號：+,-,*,/：")

import HomeWork0709.HW07091 as r
r.oper(n1,n2,op)
