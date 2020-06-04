import requests
from bs4 import BeautifulSoup
baan_list=["abnormal","agape","buem","dork","duidui","indiana","judson","khunnoo","mheenoi","buchayun",
          "dung","fyo","kids","koh","laijai","nhai","preaw","wang","wanted","work","aaum","jodeh-huesa","koom","por",
          "sod","soeiteelheemouy","indy","jo+","rang","yim"]
html="""
<html>
<head>
<style>
table, th, td {
  border: 1px solid black;
  border-collapse: collapse;
}
</style>
</head>
<body>
  <table>
    <tr>
      <th> ชื่อบ้าน </td>
      <th> สโลแกนบ้าน </td>
    </tr>
  
"""
for i in baan_list:
  request=requests.get("https://rubnongkaomai.com/baan"+"/"+i)
  soup=BeautifulSoup(request.content,"html.parser")
  baan_name=soup.find_all("h1",{"type":"header"})[0].contents[0]
  baan_slogan=[str(i) for i in soup.find_all("h3",{"type":"header"})[0].contents]
  html+="<tr><td>"+baan_name+"</td>"+"<td>"+"".join(baan_slogan)+"</td></tr>"
html+="""</table>
</body>
</html>"""
html_file=open("table.html","w",encoding="utf-8")
html_file.write(html)
html_file.close()
  


