from configparser import ConfigParser
import os
import requests
import chardet
import re
from lxml import etree
import csv
import time
from selenium import webdriver

class Demo(object):
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

    def saveData(self,data):
        date=time.strftime('%Y_%m_%d')
        path=open('D:\File\stock\\'+date+ '_test.csv','w',encoding='utf-8-sig',newline='') #notice:\'
        writer=csv.writer(path,delimiter=',')
        writer.writerows(data)

    def fetchStockData1(self):
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

        #取得页面数据，数值部分没法获取，放弃这种方法
        tr_list = [i for i in re.findall('<tr>(.*?)</tr>',text,re.S)]
        # print(tr_list)

    def fetchStockData(self):
        bro=webdriver.Chrome(executable_path=r'chromedriver.exe')
        #bro.get('https://data.eastmoney.com/zjlx/000008.html')
        bro.get('https://data.eastmoney.com/zjlx/detail.html')
        page_text=bro.page_source
        #print(page_text)

        tree=etree.HTML(page_text)
        tree1=tree.xpath('//table/tbody/tr')

        for i in range(len(tree1)):
            data=tree1[i].xpath('.//text()')
            tup1=(data[0],data[1],data[2],data[8],data[9],data[10],data[11],data[12],data[13],data[14],data[15],data[16],data[17],data[18],data[19])
            # print(tup1)
            self.saveData(data) #同一类中的函数必须传入self作为第一参数，调用方法时用self.函数名



d = Demo()
print(d.fetchStockData())


