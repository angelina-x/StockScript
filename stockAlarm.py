from configparser import ConfigParser
import os

conn = ConfigParser()
file_path = os.path.join(os.path.abspath('..//'),'configuration.ini') #os.path.join(os.getcwd(),'configuration.ini')
print('当前路径'+os.path.abspath('.'))
if not os.path.exists(file_path):
    raise FileNotFoundError("文件不存在")