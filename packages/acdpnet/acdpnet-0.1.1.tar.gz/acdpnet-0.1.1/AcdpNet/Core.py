'''
Copyright (c) 2021 https://gitee.com/intellen
Intellen - Network is licensed under Mulan PSL v2.
You can use this software according to the terms and conditions of the Mulan PSL v2. 
You may obtain a copy of Mulan PSL v2 at:
            http://license.coscl.org.cn/MulanPSL2 
THIS SOFTWARE IS PROVIDED ON AN "AS IS" BASIS, WITHOUT WARRANTIES OF ANY KIND, EITHER EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO NON-INFRINGEMENT, MERCHANTABILITY OR FIT FOR A PARTICULAR PURPOSE.  
See the Mulan PSL v2 for more details. 

File    : Core.py
Author  : Aiden
Project : Intellen
Url     : https://gitee.com/intellen/network
'''
from socket import *
import threading, queue
import ast, struct, re
import time, random

__version__ = '0.1.1'

bufsize = 2048

def RanCode(num):
    ran_str = ''.join(random.sample('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', num))
    return ran_str

def CheckIp(ip):
    compile_ip = re.compile('^(1\d{2}|2[0-4]\d|25[0-5]|[1-9]\d|[1-9])\.(1\d{2}|2[0-4]\d|25[0-5]|[1-9]\d|\d)\.(1\d{2}|2[0-4]\d|25[0-5]|[1-9]\d|\d)\.(1\d{2}|2[0-4]\d|25[0-5]|[1-9]\d|\d)$')
    if compile_ip.match(ip):return True
    else:return False

def GetIP(domain):
    addr = getaddrinfo(domain, 'http')
    return addr[0][4][0]

class Controler:
    def __init__(self, conn):
        self.conn = conn

    def recv(self):
        global bufsize
        conn = self.conn
        length = struct.unpack('i',conn.recv(4))[0]
        data = b''
        while length > bufsize:
            data += conn.recv(bufsize)
            length -= bufsize
        data += conn.recv(length)
        time.sleep(0.001)
        return data.decode('utf-8')

    def send(self, data):
        conn = self.conn
        length = len(data)
        header = struct.pack('i', length)
        time.sleep(0.0001)
        conn.send(header)
        conn.send(data)

class Orgin(threading.Thread):
    def __init__(self, conn):
        super().__init__()
        self.controler = Controler(conn)
        self.que = queue.Queue()
        self.spe = queue.Queue()

    def recv(self):
        return self.controler.recv()

    def send(self, data):
        self.controler.send(data)

class InputData(Orgin):
    def run(self):
        while True:
            req = self.que.get()
            datastr = str(req)
            try:
                self.send(datastr.encode('utf-8'))
                self.que.task_done()
            except:
                break
 
class GetData(Orgin):
    def run(self):
        while True:
            try:
                data = self.recv()
                if '_sys' in data:
                    self.spe.put(data)
                    continue
                self.que.put(data)
            except:
                break

class CoreTree:
    def __init__(self, host, port=1305):
        global __version__
        if not CheckIp(host):host = GetIP(host)
        self.addr = (host, port)
        self.conn = socket(AF_INET,SOCK_STREAM)
        self.controler = Controler(self.conn)
        self.act = False
        self.add = {
            'version':__version__,
            "file":False
        }

    def __recv(self):
        return self.controler.recv()

    def __send(self, data):
        self.controler.send(data)
    
    def connect(self, account, pwd):
        self.conn.connect(self.addr)
        data = str({"code":pwd, "account":account, "add":self.add})
        try:
            self.__send(data.encode('utf-8'))
        except:
            self.conn.close()
            return False
        result = self.__recv()
        if result == '401':
            self.conn.close()
            return False
        else:
            self.act = True
            return True
    
    def active(self):
        if not self.act:return False
        self.input = InputData(self.conn)
        self.get = GetData(self.conn)
        self.input.start()
        self.get.start()
        return True
    
    def send(self, data, recver=None):
        if recver:
            if type(data) == dict:
                req = data
                req['_recver'] = recver
            else:
                req = {'_data':data, '_recver':recver}
        else:
            if type(data) == dict:
                req = data
            else:
                req = {'_cmd':data}
        self.input.que.put(req)
        time.sleep(0.0001)

    def recv(self, wait=True):
        data = self.get.que.get(wait)
        self.get.que.task_done()
        return data