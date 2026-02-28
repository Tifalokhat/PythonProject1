# coding:utf-8
import threading
from socket import socket,AF_INET,SOCK_STREAM

import wx

class YsjClient(wx.Frame):
    def __init__(self,client_name):
        wx.Frame.__init__(self,None,id=1001,title=client_name+'的客户端',pos=wx.DefaultPosition,size=(400,450))
        pl=wx.Panel(self)
        box=wx.BoxSizer(wx.VERTICAL)
        fgz1=wx.FlexGridSizer(wx.HSCROLL)

        conn_btn=wx.Button(pl,size=(200,40),label='连接')
        dis_conn_btn=wx.Button(pl,size=(200,40),label='断开')

        fgz1.Add(conn_btn,1,wx.TOP|wx.LEFT)
        fgz1.Add(dis_conn_btn,1,wx.TOP|wx.RIGHT)
        box.Add(fgz1,1,wx.ALIGN_CENTRE)

        self.show_text=wx.TextCtrl(pl,size=(400,210),style=wx.TE_MULTILINE|wx.TE_READONLY)
        box.Add(self.show_text,1,wx.ALIGN_CENTRE)

        self.chat_text=wx.TextCtrl(pl,size=(400,120),style=wx.TE_MULTILINE)
        box.Add(self.chat_text,1,wx.ALIGN_CENTRE)

        fgz2=wx.FlexGridSizer(wx.HSCROLL)
        reset_btn=wx.Button(pl,size=(200,40),label='重置')
        send_btn=wx.Button(pl,size=(200,40),label='发送')
        fgz2.Add(reset_btn,1,wx.TOP|wx.LEFT)
        fgz2.Add(send_btn,1,wx.TOP|wx.RIGHT)

        box.Add(fgz2,1,wx.ALIGN_CENTRE)

        pl.SetSizer(box)

        '''----------------------------以上代码都是界面的绘制代码---------------------------------'''

        self.client_name=client_name
        self.isConnected=False
        self.client_socket=None
        self.Bind(wx.EVT_BUTTON, self.connect_to_server, conn_btn)
        self.Bind(wx.EVT_BUTTON,self.dis_conn_server,dis_conn_btn)

        self.Bind(wx.EVT_BUTTON,self.send_to_server, send_btn)
        self.Bind(wx.EVT_BUTTON,self.reset,reset_btn)

    def reset(self,event):
        self.chat_text.Clear()

    def dis_conn_server(self,event):
        self.client_socket.send('Y-disconnect-SJ'.encode('utf-8'))
        self.isConnected=False

    def send_to_server(self,event):
        if self.isConnected:
            input_data=self.chat_text.GetValue()
            if input_data!='':
                self.client_socket.send(input_data.encode('utf-8'))
                self.chat_text.Clear()


    def connect_to_server(self,event):
        print(f'{self.client_name}连接服务器成功')
        if not self.isConnected:
            server_host_port=('127.0.0.1',8888)
            self.client_socket=socket(AF_INET,SOCK_STREAM)
            self.client_socket.connect(server_host_port)
            self.client_socket.send(self.client_name.encode('utf-8'))
            client_thread=threading.Thread(target=self.recv_data)
            client_thread.daemon=True
            self.isConnected=True
            client_thread.start()
    def recv_data(self):
        while self.isConnected:
            data=self.client_socket.recv(1024).decode('utf-8')
            self.show_text.AppendText('-'*40+'\n'+data+'\n')
        self.client_socket.close()


if __name__ == '__main__':
    app=wx.App()
    name=input('请输入你的名字：')
    client=YsjClient(name)
    client.Show()
    app.MainLoop()

