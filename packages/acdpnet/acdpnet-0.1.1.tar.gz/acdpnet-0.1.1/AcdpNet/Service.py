'''
Copyright (c) 2021 https://gitee.com/intellen
Intellen - Network is licensed under Mulan PSL v2.
You can use this software according to the terms and conditions of the Mulan PSL v2. 
You may obtain a copy of Mulan PSL v2 at:
            http://license.coscl.org.cn/MulanPSL2 
THIS SOFTWARE IS PROVIDED ON AN "AS IS" BASIS, WITHOUT WARRANTIES OF ANY KIND, EITHER EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO NON-INFRINGEMENT, MERCHANTABILITY OR FIT FOR A PARTICULAR PURPOSE.  
See the Mulan PSL v2 for more details. 

File    : Service.py
Author  : Aiden
Project : Intellen
Url     : https://gitee.com/intellen/network
'''
import socketserver
import ast, struct
import queue, random
import time

__version__ = '0.1.1'

def RanCode(num):
    ran_str = ''.join(random.sample('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', num))
    return ran_str

def AccountCheck(account):
    able = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 @#$%^~-_=+"<>./'
    for w in account:
        if not w in able:return False
    if len(account) < 2:return False
    return True

class Node:
    '''
    Save infomation of a connection

        account(str)  : The only id of this connection
        addr(tuple)   : IP(str) and port(int)
        conn(object)  : Handler.request
    '''
    def __init__(self, account, addr, conn, add):
        self.account = account
        self.addr = addr
        self.conn = conn
        self.add = add
        self.que = queue.Queue()

class Connector:
    '''Manage nodes'''
    def __init__(self):
        self.__list = []
    
    def listall(self) -> list:
        ''' Return all the nodes' account '''
        results = {}
        for node in self.__list:
            results[node.account] = node.add
        return results
    
    def search(self, account) -> tuple:
        '''
        Search node you want by account

            account(str) : The id of node you wanna get
        '''
        for node in self.__list:
            if node.account == account:
                return True, node
        return False, None
    
    def add(self, node) -> bool:
        '''
        Add a new node which there have not the same account

            node(object) : Node(account, password, conn)
        '''
        iden = self.search(node.account)[0]
        # Check if there is a same node
        if iden != False:return False
        self.__list.append(node)
        return True
    
    def remove(self, account) -> bool:
        '''
        Delete a node which there have

            account(str)  : The id of node you wanna delete
        '''
        node = self.search(account)
        # Check if here have node you can delete
        if not node[1]:return False
        self.__list.remove(node[1])
        return True

connector = Connector()
class CoreTree(socketserver.BaseRequestHandler):
    def setup(self):
        # Set up data
        super().setup()
        # Connect here should send a code which is this so that can continue
        self.conpwd = 'sf5dfe146'
        self.bufsize = 4096
    
    def recv(self):
        conn = self.request
        length = struct.unpack('i',conn.recv(4))[0]
        buf = self.bufsize
        data = b''
        while length > buf:
            data += conn.recv(buf)
            length -= buf
        data += conn.recv(length)
        return data.decode('utf-8')

    def send(self, data, node=None):
        if not node:
            node = self.node
        conn = node.conn
        LineCode = RanCode(3)
        node.que.put(LineCode)
        print(LineCode)
        while True:
            if node.que.get() == LineCode:
                break
        length = len(data)
        header = struct.pack('i', length)
        try:
            conn.send(header)
            conn.send(data)
        except:pass
        node.que.task_done()

    def sign(self):
        # When another node connect
        global connector
        conn = self.request
        while True:
            try:data = self.recv()
            except:return False
            # Check connection and data
            if not data:continue
            else:break
        try:data = ast.literal_eval(data)
        except:return  False
        # Check data type
        if type(data) != dict:return False
        code = data.get('code')
        account = data.get('account')
        if not AccountCheck(account):return False
        # Check registration information
        if code != self.conpwd and account == '':return False
        same = connector.search(account)
        if same[0] == True:return False
        # Save the infomation
        self.node = Node(account, self.client_address, conn, data.get('add', {}))
        print(self.node.add)
        connector.add(self.node)
        # print(account, self.client_address)
        return True

    def forward(self, data):
        # Forward information to another node or group
        global connector
        conn = self.request
        # Get target account
        account = data.pop('_recver')
        if type(account) == str:
            if not AccountCheck(account):
                self.returninfo('500')
                return
            if account[0] == '[' and account[-1] == ']':
                try:account = ast.literal_eval(account)
                except:
                    self.returninfo('500')
                    return
            else:
                to = []
                to.append(account)
                account = to
        elif type(account) == list:
            pass
        else:
            self.returninfo('500')
            return
        # Check alive
        Alive = []
        for acc in account:
            stu, node = connector.search(acc)
            if stu == True:
                Alive.append(node)
        if Alive == []:
            self.returninfo('404')
            return
        # Add 'from' data
        data.setdefault('_from',self.node.account)
        if len(account) > 1:
            account.append(self.node.account)
            data.setdefault('_group',account)
        # Send to
        data = str(data).encode('utf-8')
        for node in Alive:
            self.send(data, node)
        time.sleep(0.0001)
        return True
    
    def command(self, data):
        global connector
        cmd = data.get('_cmd')
        if cmd == 'alive':
            Alive = connector.listall()
            Alive['_sys'] = data.get('_sys', '')
            self.returninfo(str(Alive))
            return

    def returninfo(self, info):
        self.send(info.encode('utf-8'))

    def handle(self):
        global connector
        if self.sign() == False:
            try:self.returninfo('401')
            except:pass
        else:
            self.returninfo('OK')
            conn = self.request
            while True:
                try:data = self.recv()
                except:break
                try:data = ast.literal_eval(data)
                except:
                    self.returninfo('DataError')
                    continue
                if '_recver' in data:
                    self.forward(data)
                    continue
                if '_cmd' in data:
                    print(data)
                    self.command(data)
                    continue
            connector.remove(self.node.account)

if __name__ == '__main__':
    addr = ('0.0.0.0',1305)
    server = socketserver.ThreadingTCPServer(addr,CoreTree)
    server.serve_forever()