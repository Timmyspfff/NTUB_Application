import requests
from lxml import etree
from bs4 import BeautifulSoup
import pandas as pd

url = "https://ntcbadm1.ntub.edu.tw/login.aspx"
url1 = 'https://ntcbadm1.ntub.edu.tw/HttpRequest/Login.ashx'

UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36 Edg/99.0.1150.46"
headers = { "User-Agent" : UA,
"Referer": "https://ntcbadm1.ntub.edu.tw/logout.aspx"
}
session = requests.Session()

page = session.get('https://ntcbadm1.ntub.edu.tw/login.aspx')
soup = BeautifulSoup(page.content, 'lxml')


# 解析驗證碼圖片地址
page_text = session.get(url = url,headers = headers).text
tree = etree.HTML(page_text)
img_src = 'https://ntcbadm1.ntub.edu.tw/' + tree.xpath('//*[@id="Validation_Image"]/@src')[0]
# 將驗證碼圖片儲存到本地
img_data = session.get(img_src,headers = headers).content
with open('./code.jpg','wb') as fp:
    fp.write(img_data)

#輸入你的學號、密碼、驗證碼
# user=input("請輸入學號")
# password=input("請輸入密碼")
captcha=input("請輸入驗證碼")
payload_loginData={
    'Type':'0',"UserID":'10946021',"PWD":'spfff1928','loginbtn':''}
payload_loginData['__VIEWSTATE'] = soup.select_one('#__VIEWSTATE')['value']
payload_loginData['__VIEWSTATEGENERATOR'] = soup.select_one('#__VIEWSTATEGENERATOR')['value']


payload_captcha = {'CheckCode': captcha,
'Model': 'Check_Code_TF'}

res=session.post(url,headers=headers,data=payload_loginData)
res1=session.post(url1,headers=headers,data=payload_captcha)

# ke='https://ntcbadm1.ntub.edu.tw/Portal/indexSTD.aspx'
ke = 'https://ntcbadm1.ntub.edu.tw/STDWEB/Sel_Student.aspx'

# html =session.get(ke)
aaa = pd.read_html(ke)
len(aaa)
df = aaa[0]
# df
# 
# print(html.text)