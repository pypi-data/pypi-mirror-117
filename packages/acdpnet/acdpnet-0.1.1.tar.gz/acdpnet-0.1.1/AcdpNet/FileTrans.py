'''
Copyright (c) 2021 https://gitee.com/intellen
Intellen - Network is licensed under Mulan PSL v2.
You can use this software according to the terms and conditions of the Mulan PSL v2. 
You may obtain a copy of Mulan PSL v2 at:
            http://license.coscl.org.cn/MulanPSL2 
THIS SOFTWARE IS PROVIDED ON AN "AS IS" BASIS, WITHOUT WARRANTIES OF ANY KIND, EITHER EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO NON-INFRINGEMENT, MERCHANTABILITY OR FIT FOR A PARTICULAR PURPOSE.  
See the Mulan PSL v2 for more details. 

File    : FileTrans.py
Author  : Aiden
Project : Intellen
Url     : https://gitee.com/intellen/network
'''
from socket import *
import threading, queue
import ast, struct, re
import time, random
import platform
import ast, queue
import os

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

def listdir(path):
    if os.path.exists(path) == True:
        dat = {"files":[],"folders":[],"unknows":[]}
        for i in os.listdir(path):
            if os.path.isdir(path + i) == True:
                dat["folders"].append(i)
            elif os.path.isfile(path + i) == True:
                dat["files"].append(i)
            else:
                dat["unknows"].append(i)
        return dat

class Command(threading.Thread):
    def __init__(self, tree):
        super().__init__()
        self.tree = tree
    
    def file(self, data):
        todo = data['_cmd']
        del data['_cmd']
        cmd = todo.get("cmd", "list")
        if cmd == "list":
            path = todo.get("path")
            try:
                result = listdir(path)
            except:
                result = {"rs":"PathError"}
            data["_result"] = result
            self.tree.send(str(data).encode('utf-8'))
            
    def run(self):
        while True:
            data = self.tree.cmds.get()
            self.tree.cmds.task_done()
            data = ast.literal_eval(data)
            todo = data['_cmd']
            if type(todo) == str:
                result = os.popen(todo)
                result = result.read()
                req = data
                req['_result'] = result
                req['_recver'] = req['_from']
                del req['_from']
                del req['_cmd']
                self.tree.send(str(req).encode('utf-8'))
            elif type(todo) == dict:
                data['_recver'] = data['_from']
                del data['_from']
                self.file(data)

class GetData_File(Orgin):
    def run(self):
        self.cmds = queue.Queue()
        self.cmd = Command(self)
        self.cmd.start()
        while True:
            try:
                data = self.recv()
                if '_cmd' in data:
                    self.cmds.put(data)
                    continue
                if '_sys' in data:
                    self.spe.put(data)
                    continue
                self.que.put(data)
            except:
                break

class Transfer(CoreTree):
    def __init__(self, host, port=1305):
        super().__init__(host, port=1305)
        self.add['file'] = True
        self.add['system'] = platform.platform()
    
    def active(self):
        if not self.act:return False
        self.input = InputData(self.conn)
        self.get = GetData_File(self.conn)
        self.input.start()
        self.get.start()
        return True
    
    def check(self, dev):
        LineCode = RanCode(3)
        self.send({'_cmd':'alive', '_sys':LineCode})
        while True:
            try:result = ast.literal_eval(self.get.spe.get(timeout=5))
            except:
                result = {}
                break
            if result.get('_sys') == LineCode:
                self.get.spe.task_done()
                break
        target = result.get(dev, {'file':False})
        if target['file'] == False:return False,
        return True
    
    def cmd(self, target, cmd):
        able = self.check(target)
        if not able:return False
        LineCode = RanCode(3)
        req = {
            '_cmd':cmd,
            '_sys':LineCode,
        }
        self.send(req, target)
        while True:
            try:result = ast.literal_eval(self.get.spe.get(timeout=5))
            except:
                result = {}
                break
            if result.get('_sys') == LineCode:
                self.get.spe.task_done()
                break
        return result.get('_result', '404')
    
    def file(self, mode, target, path):
        able = self.check(target)
        if not able:return False
        LineCode = RanCode(3)
        if mode == "list":
            req = {
                '_cmd':{"cmd":"list", "path":path},
                '_sys':LineCode,
            }
        else:return False
        self.send(req, target)
        while True:
            try:result = ast.literal_eval(self.get.spe.get(timeout=5))
            except:
                result = {}
                break
            if result.get('_sys') == LineCode:
                self.get.spe.task_done()
                break
        if mode == "list":
            return result.get('_result', '404')