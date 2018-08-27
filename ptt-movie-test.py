#ptt movie板
# 抓取網頁資料
import urllib.request as request
#下兩行為mac需求
import ssl
context=ssl._create_unverified_context()
#url="https://www.ptt.cc/bbs/Gossiping/index.html"
for i in range(7020,7019,-1):
    url="https://www.ptt.cc/bbs/movie/index"+str(i)+".html"
    print(url)
#sys.exit() #可以只執行到這邊

#偽裝成真實的連線 #大小寫要注意一下
    req=request.Request(url, headers={
            
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"
        
     })

    with request.urlopen(req,context=context) as response:
        data=response.read().decode("utf-8")

    print("=============")

    # 使用BeautifulSoup 擷取目標文字
    import bs4
    root= bs4.BeautifulSoup(data, "html.parser")


    titles=root.find_all("div","title") #找出<div class="title">...</div>

    for titles in titles:
        try:
            print(titles)
        except AttributeError:
            continue

