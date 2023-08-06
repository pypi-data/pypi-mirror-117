from downloader import *
from PyQt5.Qt import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys
import requests
import os
import datetime
import time
class window(QtWidgets.QMainWindow,Ui_MainWindow):
    def __init__(self):
        super(window,self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.download)
        self.te = ''
        self.progressBar.setValue(0)
    def download(self):
        self.u(0)
        a = datetime.datetime.now()
        self.u(1)
        self.te = ''
        self.u(3)
        self.textBrowser.setText(self.te)
        self.u(4)
        self.update('initlazing')
        self.u(5)

        try:
            self.u(10)
            self.update('getting')
            self.u(20)
            r = requests.get(self.lineEdit.text(),headers = {'user-agent':
                                                             'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36 Edg/92.0.902.78'})
            self.u(30)
            con = r.content
            self.u(40)
            text = self.lineEdit.text().split('/')
            self.u(50)
            self.update('downloading')
            self.u(60)
            aaaaa = self.lineEdit_2.text()+text[-1].replace('/','')\
            .replace(r'\\', '')\
            .replace(':', '')\
            .replace('*', '')\
            .replace('?', '')\
            .replace('"','') \
            .replace('<', '') \
            .replace('>', '') \
            .replace('|', '') \

            aaa = str(time.time())
            with open(aaaaa,'ab+') as f:
                self.u(70)
                self.update('writing')
                self.u(80)
                f.write(con)
                self.u(90)
            self.u(101)
            b = datetime.datetime.now()
            x = b-a
            x = x.total_seconds()
            size = float(os.path.getsize(aaaaa))
            if size >= 1024 and size <= 1024*1024:
                self.update(f'sucsess in {x}s({size/1024}KB,{size/1024/x}KB/s)')
            elif size >= 1024*1024 and size <= 1024*1024*1024:
                self.update(f'sucsess in {x}s({size/1024/1024}MB,{size/1024/1024/x}MB/s)')
            elif size >= 1024*1024*1024 and size <= 1024*1024*1024*1024:
                self.update(f'sucsess in {x}s({size/1024/1024/1024}GB,{size/1024/1024/1024/x}GB/s)')
            elif size >= 1024*1024*1024*1024:
                self.update(f'sucsess in {x}s({size/1024/1024/1024/1024}TB,{size/1024/1024/1024/1024/x}TB/s)')
            else:
                self.update(f'sucsess in {x}s({size}B,{size/x}B/s)')
        except BaseException as e:
            self.u(0)
            self.update(f'error:{e}')





    def update(self,t):
        self.te += t + '\n'
        self.textBrowser.setText(self.te)
    def u(self,v):
        a = self.progressBar.value()
        if v > a:
            for i in range(a,v):
                self.progressBar.setValue(i)
                time.sleep(0.001)
        else:

            self.progressBar.setValue(v)



app = QtWidgets.QApplication(sys.argv)
window = window()
window.show()
sys.exit(app.exec_())



