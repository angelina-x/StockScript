from configparser import ConfigParser
import os
import requests
import chardet
import re
from lxml import etree
import csv

class ReadConfigFile(object):
    def read_config(self):
        conn = ConfigParser()
        file_path = os.path.join(os.path.abspath('.'),'configuration.ini') #os.path.join(os.getcwd(),'configuration.ini')
        file_path1= os.path.join(os.getcwd(),'configuration.ini')
        print('当前路径'+os.path.abspath('.'))
        print("file_path:"+file_path)
        print("file_path1:"+file_path1)
        if not os.path.exists(file_path):
            raise FileNotFoundError("文件不存在")

        conn.read(file_path,encoding='utf-8')
        mail_host=conn.get('email','mail_host')
        mail_user=conn.get('email','mail_user')
        mail_pass=conn.get('email','mail_pass')
        sender=conn.get('email','sender')
        receivers=conn.get('email','receivers').split(',')
        return [mail_host,mail_user,mail_pass,sender,receivers] 
        
rc = ReadConfigFile()
print(rc.read_config())



headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36',
    #在爬虫里面如果出现了Referer最好也粘上去，因为有时候服务器会根据Referer来判断请求时由浏览器还是爬虫发出的
    'Referer':'https://www.douban.com/'
}
#url = "https://data.eastmoney.com/zjlx/detail.html"
url = "https://data.eastmoney.com/zjlx/000008.html"
response = requests.get(url,headers=headers)#发起请求得到响应
response.encoding = "utf-8"
text = response.text#返回一个经过解码的字符串
#print(text)

comments_list = [i for i in re.findall('<tr>(.*?)</tr>',text,re.S)]

print(comments_list)