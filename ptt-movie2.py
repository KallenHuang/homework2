#ptt movie板時間線-電影話題性
# 抓取網頁資料
import string
name=input(str("搜尋電影關鍵字："))

import urllib.request as request
#下兩行為mac需求
import ssl
import sys
context=ssl._create_unverified_context()
#url="https://www.ptt.cc/bbs/Gossiping/index.html"

def newestPageNamber():
    context=ssl._create_unverified_context()

    url="https://www.ptt.cc/bbs/movie/index.html"
    #print(url)
    #偽裝成真實的連線 #大小寫要注意一下
    req=request.Request(url, headers={
            
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"
        
        })
    with request.urlopen(req,context=context) as response:
        data=response.read().decode("utf-8")
    #print("=============")
    # 使用BeautifulSoup 擷取目標文字
    import bs4
    root= bs4.BeautifulSoup(data, "html.parser")

    nextLink=root.find("a",string="‹ 上頁") #對著<上頁>的連結按鈕點右鍵選檢查，然後再複製檢查裡面的<‹ 上頁>貼上
    next=nextLink["href"]
    listnew=list(next)
    #print(listnew[16:20])
    newestPN=''.join(listnew[16:20])
    #print(newestPN)
    newestPN1=int(newestPN)+1
    return newestPN1

def search(n1,n2):

    k=0
    nameNumber=0
    timelist=[]
    for i in range(n1,n2,-1):
        url="https://www.ptt.cc/bbs/movie/index"+str(i)+".html"
        #print(url)
        req=request.Request(url, headers={  
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"
            ,"Cookie": "over18=1"
        })

        with request.urlopen(req,context=context) as response:
            data=response.read().decode("utf-8")

        k+=1
        print("=",k,"=")
        # 使用BeautifulSoup 擷取目標文字
        import bs4
        root= bs4.BeautifulSoup(data, "html.parser")
        titles=root.find_all("div","r-ent")
        

        
        for titles in titles: #將div的部份進行迴圈
            
            try:    #主要是為了except出現"本文已被刪除"這樣沒有a的部分
                listmv=(titles.a.string) #將a的部份轉為列表，名為listmv
                #print(listmv)
                listtime=titles.find("div","date")
                listtimes=(listtime.string)
                #print(listtimes)
                if name in str(listmv):
                    strlistmv=str(listmv)
                    print(strlistmv)
                    print(listtimes)
                    #s=str(listtimes)
                    timelist.append(listtimes)
                    # nameNumber+=1
                    # listtime=(time.string)
                    # print(listtime)
                

            except AttributeError:  #把有因為"本文已被刪除"出現錯誤訊息AttributeError的部份跳過
                continue
        #print(nameNumber)
    return{"nameNumber":nameNumber,"timelist":timelist}

rr=int(input("搜尋頁數："))
n1=int(newestPageNamber())
n2=n1-rr


#search(n1,n2)
data=search(n1,n2)
# N=data["nameNumber"]
N=data["timelist"]
#print(N)#所有日期(有重複))
print("總共搜尋筆數：",len(data["timelist"]))#總共找到幾筆
q=len(data["timelist"])
#去掉重複串列之後不改變順序的作法
l1 = N
setdate = []
for i in l1:
    if not i in setdate:
        setdate.append(i)
#print(setdate)#篩選掉重複的日期(不重複)
a=len(setdate)#不重複的日期數
print("~~~~~~~~~~")
m=0
setdateNumber=[]
for m in range(a):
    dateN=int(N.count(setdate[m]))
    #print(dateN)#相同日期的筆數
    m+=1
    setdateNumber.append(dateN)#相同日期的筆數串列
#print(setdateNumber)#相同日期的"筆數"串列後印出

#再一次解決問題
s=0
qsetdateNumber=[]
for m in range(a):
    dateN=int(N.count(setdate[s]))
    #print(dateN)#相同日期的筆數
    s+=1
    qsetdateNumber.append(dateN)#相同日期的筆數串列
#print(setdateNumber)#相同日期的"筆數"串列後印出


JAN="1/"
FEB="2/"
MAR="3/"
APR="4/"
MAY="5/"
JUN="6/"
JUL="7/"
AUG="8/"
SEP="9/"
OCT="10/"
NOV="11/"
DEC="12/"

n=0
listk=[]

for howmuch in range(a):
    if NOV in setdate[n]:
        k=int(setdate[n].replace("11/", "304"))
    elif DEC in setdate[n]:
        k=int(setdate[n].replace("12/", "334"))
    elif MAR in setdate[n]:
        k=int(setdate[n].replace("3/", "59"))
    elif APR in setdate[n]:
        k=int(setdate[n].replace("4/", "90"))
    elif MAY in setdate[n]:
        k=int(setdate[n].replace("5/", "120"))
    elif JUN in setdate[n]:
        k=int(setdate[n].replace("6/", "151"))
    elif JUL in setdate[n]:
        k=int(setdate[n].replace("7/", "181"))
    elif AUG in setdate[n]:
        k=int(setdate[n].replace("8/", "212"))
    elif SEP in setdate[n]:
        k=int(setdate[n].replace("9/", "243"))
    elif OCT in setdate[n]:
        k=int(setdate[n].replace("10/", "273"))
    elif FEB in setdate[n]:
        k=int(setdate[n].replace("2/", "31"))
    elif JAN in setdate[n]:
        k=int(setdate[n].replace("1/", ""))
    else:
        print("no")
    n+=1
    d=int(k/100)
    if d==0:
        d=1
    b=k%d
    c=d+b
    #print(c)
    listk.append(c)
print(listk)#日期轉化為數字

#跨年數字調整
b=len(listk)
print("b=",b)
x=0
for i in range(b-1):
    s1=listk[:x+1]
    s2=listk[x+1:]
    if listk[x]-listk[x+1]<-300:
        y=0
        for i in range(b-x-1):
            print("ok")
            s2[y]=s2[y]-365
            y+=1
            print("y=",y)
        print("s2=",s2)
        s3=s1+s2
        print("s1+s2=",s3)  
    else:
        s3=listk 
    x+=1     
print("第一次s3",s3)






maxlistk=max(s3)
minlistk=min(s3)
minlistk1=min(s3)-1
print("最大值為",maxlistk,"最小值為",minlistk)
rrlistk=maxlistk-minlistk
print(rrlistk)
s3.sort()
s3.reverse()
print(s3)



#sys.exit()

h=0
for qq in range(rrlistk):
    if s3[h]-1 != s3[h+1]:
        s3.insert(h+1,s3[h]-1)
        setdateNumber.insert(h+1,0)
        qsetdateNumber.insert(h+1,0)
        h+=1
    else:
        h+=1
        

#print(listk)

day=["12/31","12/30","12/29","12/28","12/27","12/26","12/25","12/24","12/23","12/22","12/21","12/20","12/19","12/18","12/17","12/16","12/15","12/14","12/13","12/12","12/11","12/10","12/9","12/8","12/7","12/6","12/5","12/4","12/3","12/2","12/1","11/30","11/29","11/28","11/27","11/26","11/25","11/24","11/23","11/22","11/21","11/20","11/19","11/18","11/17","11/16","11/15","11/14","11/13","11/12","11/11","11/10","11/9","11/8","11/7","11/6","11/5","11/4","11/3","11/2","11/1","10/31","10/30","10/29","10/28","10/27","10/26","10/25","10/24","10/23","10/22","10/21","10/20","10/19","10/18","10/17","10/16","10/15","10/14","10/13","10/12","10/11","10/10","10/9","10/8","10/7","10/6","10/5","10/4","10/3","10/2","10/1","9/30","9/29","9/28","9/27","9/26","9/25","9/24","9/23","9/22","9/21","9/20","9/19","9/18","9/17","9/16","9/15","9/14","9/13","9/12","9/11","9/10","9/9","9/8","9/7","9/6","9/5","9/4","9/3","9/2","9/1","8/31","8/30","8/29","8/28","8/27","8/26","8/25","8/24","8/23","8/22","8/21","8/20","8/19","8/18","8/17","8/16","8/15","8/14","8/13","8/12","8/11","8/10","8/9","8/8","8/7","8/6","8/5","8/4","8/3","8/2","8/1","7/31","7/30","7/29","7/28","7/27","7/26","7/25","7/24","7/23","7/22","7/21","7/20","7/19","7/18","7/17","7/16","7/15","7/14","7/13","7/12","7/11","7/10","7/9","7/8","7/7","7/6","7/5","7/4","7/3","7/2","7/1","6/30","6/29","6/28","6/27","6/26","6/25","6/24","6/23","6/22","6/21","6/20","6/19","6/18","6/17","6/16","6/15","6/14","6/13","6/12","6/11","6/10","6/9","6/8","6/7","6/6","6/5","6/4","6/3","6/2","6/1","5/31","5/30","5/29","5/28","5/27","5/26","5/25","5/24","5/23","5/22","5/21","5/20","5/19","5/18","5/17","5/16","5/15","5/14","5/13","5/12","5/11","5/10","5/9","5/8","5/7","5/6","5/5","5/4","5/3","5/2","5/1","4/30","4/29","4/28","4/27","4/26","4/25","4/24","4/23","4/22","4/21","4/20","4/19","4/18","4/17","4/16","4/15","4/14","4/13","4/12","4/11","4/10","4/9","4/8","4/7","4/6","4/5","4/4","4/3","4/2","4/1","3/31","3/30","3/29","3/28","3/27","3/26","3/25","3/24","3/23","3/22","3/21","3/20","3/19","3/18","3/17","3/16","3/15","3/14","3/13","3/12","3/11","3/10","3/9","3/8","3/7","3/6","3/5","3/4","3/3","3/2","3/1","2/28","2/27","2/26","2/25","2/24","2/23","2/22","2/21","2/20","2/19","2/18","2/17","2/16","2/15","2/14","2/13","2/12","2/11","2/10","2/9","2/8","2/7","2/6","2/5","2/4","2/3","2/2","2/1","1/31","1/30","1/29","1/28","1/27","1/26","1/25","1/24","1/23","1/22","1/21","1/20","1/19","1/18","1/17","1/16","1/15","1/14","1/13","1/12","1/11","1/10","1/9","1/8","1/7","1/6","1/5","1/4","1/3","1/2","1/1"]
maxlistk365=365-maxlistk
maxminlistk1=maxlistk-minlistk+1

del day[:maxlistk365]
del day[maxminlistk1:]
#print(setdateNumber)#缺少日期補零的篇數計算
#print(day)          #缺少日期補齊


q=len(setdateNumber)-1

z=0
for add in range(q):
    addnumber=setdateNumber[q]+setdateNumber[q-1]
    #print(addnumber)
    setdateNumber[q-1]=addnumber
    addsetdateNumber=setdateNumber
    q-=1

#print(addsetdateNumber)#缺少日期補零的篇數計算(累加後的)


#曲線圖
import plotly.plotly as py
import plotly.graph_objs as go

# Add data
day.reverse()

addsetdateNumber.reverse()
#print(addsetdateNumber)
qsetdateNumber.reverse()


# Create and style traces
trace0 = go.Scatter(
    x = day,
    y = addsetdateNumber,
    name = "<"+name+'>累計文章數',
    line = dict(
        color = ('rgb(205, 12, 24)'),
        width = 4)
)

trace1 = go.Scatter(
    x = day,
    y = qsetdateNumber,
    name = "<"+name+">當日文章數",
    line = dict(
        color = ('rgb(22, 96, 167)'),
        width = 4,)
)

data = [trace0, trace1]

# Edit the layout
layout = dict(title = "電影<"+name+">於PTT話題度統計",
              xaxis = dict(title = '日期'),
              yaxis = dict(title = '文章數'),
              )

fig = dict(data=data, layout=layout)
py.plot(fig,filename="mychart",auto_open=True)




