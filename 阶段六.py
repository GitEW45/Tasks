import requests
import re
import os

headers={
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 SLBrowser/8.0.0.12022 SLBChan/105'
}
#获取网页源代码
response=requests.get('https://itawenya.cn/oldindex.html')
text=response.text
#获取网站图片的链接
image_list=re.findall('<img src="(.*?)" width="209" height="190" alt=".*?"/>'.text)
#匹配网站文字
pattern=r'<p>(.+?)</p>'
introduction=re.findall(pattern,content)
if introduction:
   introduction="\n".join(introduction)
   introduction=re.sub('(&ensp;)|(&nbsp;)|(<a href.*?</a>>)',"",introduction)
#设置储存路径
path=r"C:\Users\wcjR7000\Desktop\imgs"
if not os.path.exists(path):
    os.mkdir(path)
#下载图片
index=0
for item in image_list:
   response=requests.get(item,headers=headers)
   with open(path+'\\'str(index)+'.jpg'.'wb') as f:
    f.write(reesponse,content)
    print(path+'\\'+str(index)+'jpg'+"下载成功")
index +=1
#写入本地文件
with open(name+".txt","w",encoding-"utf8") as fp: 
    fp.write(introduction)