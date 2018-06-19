n1=input("Enter a Number called A: ")
n2=input("Enter a Number called B: ")
n3=input("Enter a Number called C: ")
n4=input("Enter a Number called D: ")
n5=input("Enter a Number called E: ")
n1=int(n1)
n2=int(n2)
n3=int(n3)
n4=int(n4)
n5=int(n5)
sum=n1+n2+n3+n4+n5
sum=str(sum) #如果是int無法與字串連接，故重新定義為字串
print("The sum number is "+sum) #用字串相連的方式表示
list1=(n1,n2,n3,n4,n5) #建立一個列表，之後方便用max取最大值
list2=(6,7,8,9,10)
print("The biggest number is ",max(list1)) #其實用逗號就可將不同型態組合列印了
print("The smallest number is ",min(list1)) #取最小值
print("The number you typed in is ",len(list1)) #取數目
print (list2)
print (list1,list2)
#關於cmp的指令一直都有錯誤，但是查不出是什麼原因
print(list1[1:4]) #不包含4

list1=[int(input("輸入數字：")) for x in range (5)]
print(max(list1))

