#ptt movie板
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

def origin(n1,n2):
    
    for i in range(n1,n2,-1):
        url="https://www.ptt.cc/bbs/movie/index"+str(i)+".html"
        #print(url)
        req=request.Request(url, headers={  
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"
            ,"Cookie": "over18=1"
        })

        with request.urlopen(req,context=context) as response:
            data=response.read().decode("utf-8")
        
        print("===")
        # 使用BeautifulSoup 擷取目標文字
        import bs4
        root= bs4.BeautifulSoup(data, "html.parser")
        titles=root.find_all("div","title") #找出<div class="title">...</div>

        for titles in titles: #將div的部份進行迴圈
            try:    #主要是為了except出現"本文已被刪除"這樣沒有a的部分
                listmv=[titles.a.string] #將a的部份轉為列表，名為listmv
                if name in str(listmv):  #之後就能以列表方式來搜尋自定關鍵字"name"
                    print(listmv)

            except AttributeError:  #把有因為"本文已被刪除"出現錯誤訊息AttributeError的部份跳過
                continue


def search(n1,n2):
    g=0
    b=0
    s=0
    k=0
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
        titles=root.find_all("div","title") #找出<div class="title">...</div>

        for titles in titles: #將div的部份進行迴圈
            try:    #主要是為了except出現"本文已被刪除"這樣沒有a的部分
                listmv=[titles.a.string] #將a的部份轉為列表，名為listmv
                if name in str(listmv):  #之後就能以列表方式來搜尋自定關鍵字"name"
                    #print(listmv)
                    strlistmv=str(listmv)
                    goodly=strlistmv.find("好雷")
                    badly=strlistmv.find("負雷")
                    sosoly=strlistmv.find("普雷")
                    #print(goodly)
                    if goodly!=-1:
                        print(listmv)
                        g+=1
                    elif badly!=-1:
                        print(listmv)
                        b+=1
                    elif sosoly!=-1:
                        print(listmv)
                        s+=1
            except AttributeError:  #把有因為"本文已被刪除"出現錯誤訊息AttributeError的部份跳過
                continue
    return{
        "goodly":g,
        "badly":b,
        "sosoly":s}

rr=int(input("搜尋頁數："))
print("是否從最新頁開始搜尋？","\n","是，請輸入1","\n","否，請輸入2")
nn=int(input("輸入："))
if nn==1:
    n1=int(newestPageNamber())
else:
    n1=int(input("從第幾頁開始搜尋："))
n2=n1-rr

#listfound=str(search(n1,n2))
#print(search(n1,n2))

#sys.exit()
# goodly="好雷"
# if goodly in str(search(n1,n2)):
#     print(search(n1,n2))
#origin(n1,n2)

data=search(n1,n2)
#print(data["goodly"])
#sys.exit()

#圓餅圖
import plotly.plotly as py
import plotly.graph_objs as go
#建立資料
#建立圓餅圖的資料：1.labels 2.values
g=data["goodly"]
b=data["badly"]
s=data["sosoly"]
print("～～～～～～～～～～～～～～～～～～")
print("搜尋電影<",name,">在PTT最新文章",rr,"頁","\n","總共搜尋到",g+b+s,"篇文章","\n","好雷：",g,"\n","負雷：",b,"\n","普雷：",s)
print("～～～～～～～～～～～～～～～～～～")

name=str(name)
rr=str(rr)
allgbs=str(g+b+s)
bigname=name[0:5]+"\n"+name[5:]

if len(name)>5:
    newname=bigname
else:
    newname=name


#sys.exit()

fig = {
  "data": [
    {
      "values": [g, b, s],
      "labels": [
        "好雷",
        "負雷",
        "普雷"
      ],"marker":{
          "colors":[
              "rgb(142,194,255)",
              "rgb(253,148,167)",
              "rgb(143,246,136)"
          ]
      },
      "domain": {"x": [0.4, 0.7],"y": [0.4, 0.9]},
      "name": newname,
      "hoverinfo":"label+percent+name",
      "hole": .4,
      "type": "pie"
    }],
  "layout": {
        "title":("電影<"+name+">PTT最新評價共"+rr+"頁統計"+"<br>"+"統計數量"+allgbs+"筆"),
        "annotations": [
            {
                "font": {
                    "size": 20
                },
                "showarrow": False,
                "text": newname,
                "x": 0.55,
                "y": 0.65
            }
            
        ]
    }
}

#畫圖
py.plot(fig,filename="mychart",auto_open=True)