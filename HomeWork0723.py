#作業：去連結這個景點資料並找特定捷運站附近的景點，然後放到一個檔案裡
import urllib.request as request
import json
scr="http://data.taipei/opendata/datalist/apiAccess?scope=resourceAquire&rid=36847f3f-deff-4183-a5bb-800737591de5"
with request.urlopen(scr) as response:
    data=json.load(response)
#    data=response.read().decode("utf-8")
klist=data["result"]["results"]
# for MRTname in klist:
#     print(MRTname["MRT"])
# for Titlename in klist:
#     print(Titlename["stitle"])
name=input("想知道捷運站附近景點？"+"\n"+"輸入一個捷運站名稱：")
print("= = = = = = = = = = = = = =")

k=0
for Total in klist:
#    print(str(Total["MRT"])+str("：")+str(Total["stitle"]))
    if name == Total["MRT"]:
        print(str(Total["MRT"])+str("：")+str(Total["stitle"]))
        k+=1
#print(k)
print("= = = = = = = = = = = = = =")

if k==0:
    print("查無此站名")
else:
    print(str("總共有")+str(k)+str("筆資料"))

# for company in list:
#     if keyword in company["公司名稱"]: #如果輸入的字與公司名稱那個欄位有吻合
#         print(company["公司名稱"]) #則印出那個公司名稱

with open("HomeWork0723.txt","w",encoding="utf-8") as file:
    file.write("您查詢的捷運站名為："+str(name)+"\n")
    file.write("= = = = = = = = = = = = = ="+"\n")
    file.write(str(name)+"站附近的景點包含："+"\n")
    for Total in klist:
        if name == Total["MRT"]:
            file.write(str(Total["stitle"])+"\n")
    file.write("= = = = = = = = = = = = = =")
    if k==0:
        file.write("\n"+"查無此站名")
    else:
        file.write("\n"+str("總共有")+str(k)+str("筆資料"))
    