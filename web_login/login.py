import requests
from lxml import etree
from bs4 import BeautifulSoup
import pandas as pd

url = "https://ntcbadm1.ntub.edu.tw/login.aspx"


UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36 Edg/99.0.1150.46"
headers = { "User-Agent" : UA,
"Referer": "https://ntcbadm1.ntub.edu.tw/logout.aspx"
}
session = requests.Session()

page = session.get('https://ntcbadm1.ntub.edu.tw/login.aspx')
soup = BeautifulSoup(page.content, 'lxml')

page_text = session.get(url = url,headers = headers).text
tree = etree.HTML(page_text)

payload_loginData={
    "UserID":'10946021',"PWD":'spfff1928','loginbtn':''}
payload_loginData['__VIEWSTATE'] = soup.select_one('#__VIEWSTATE')['value']
payload_loginData['__VIEWSTATEGENERATOR'] = soup.select_one('#__VIEWSTATEGENERATOR')['value']


res=session.post(url,headers=headers,data=payload_loginData)

ke = 'https://ntcbadm1.ntub.edu.tw/STDWEB/Sel_Student.aspx'

html =session.get(ke)
aaa = pd.read_html(html.text)[9]
bb = pd.DataFrame(aaa)
print(bb)
