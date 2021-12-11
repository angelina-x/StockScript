from configparser import ConfigParser
import os

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