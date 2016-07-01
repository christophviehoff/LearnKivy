# File name: layouts.py
import kivy
kivy.require('1.9.0')
import socket

#install_twisted_rector must be called before importing the reactor
from kivy.support import install_twisted_reactor
install_twisted_reactor()


#A simple Client that send messages to the echo server
from twisted.internet import reactor, protocol

class EchoClient(protocol.Protocol):
    def connectionMade(self):
        self.factory.app.on_connection(self.transport)

    #core receive here
    def dataReceived(self, data):
        self.factory.app.print_message(data)

class EchoFactory(protocol.ClientFactory):
    protocol = EchoClient

    def __init__(self, app):
        self.app = app

    def clientConnectionLost(self, conn, reason):
        self.app.print_header ("---connection lost")
        self.app.header.color=(1,0,0,1)

    def clientConnectionFailed(self, conn, reason):
        self.app.print_header ("---connection failed")
        self.app.header.color=(1,0,0,1)


from kivy.app import App
from kivy.config import Config
from kivy.uix.gridlayout import GridLayout
from kivy.properties import ObjectProperty
from kivy.clock import Clock

class MyGridLayout(GridLayout):

    connection = None

    message = ObjectProperty(None)
    textbox = ObjectProperty(None)
    header  = ObjectProperty(None)


    def connect_to_server(self):
        #using self.ids.... this time instead of object property
        self.nickname = self.ids.title.text
        reactor.connectTCP('localhost', 8000, EchoFactory(self))
        host_name = socket.gethostname()
        ip_address = socket.gethostbyname(host_name)
        self.ids.hostname.text=host_name+':'+ip_address


    def disconnect(self):
        self.print_header ('---disconnecting')
        self.header.color=(1,0,0,1)
        if self.connection:
            self.connection.loseConnection()
            del self.connection

    def connection_state(self):
        if self.ids.switch.active:
            self.connect_to_server()
        else:
            self.disconnect()



    def on_connection(self, connection):
        self.print_header (self.nickname +" connected successfully!")
        self.header.color=(0,1,0,1)
        self.connection = connection


    #core send stuff here
    def send_message(self, *args):
        msg = self.textbox.text
        if msg and self.connection:
            self.connection.write("%s : %s" % (self.nickname,self.textbox.text))
            self.textbox.text = ""

    def print_message(self, msg):
        self.message.text = msg

    def print_header(self, msg):
        self.header.text = msg

    #keypad matrix callbacks

    def cb_msg_bit1(self):
        self.print_message ('bit 1 event callback')
    def cb_msg_bit2(self):
        self.print_message ('bit 2 event callback')
    def cb_msg_bit3(self):
        self.print_message ('bit 3 event callback')
    def cb_msg_bit4(self):
        self.print_message ('bit 4 event callback')
    def cb_msg_bit5(self):
        self.print_message  ('bit 5 event callback')
    def cb_msg_bit6(self):
        self.message.text = 'bit 6 event callback'
    def cb_msg_bit7(self,*args):
        self.message.text = 'bit 7 event callback'
    def cb_msg_bit8(self):
        self.message.text = 'bit 8 event callback'
    def cb_msg_bit9(self):
        self.message.text = 'bit 9 event callback'
    def cb_msg_bit10(self):
        self.message.text = 'bit 10 event callback'
    def cb_msg_bit11(self):
        self.message.text = 'bit 11 event callback'
    def cb_msg_bit12(self):
        self.message.text = 'bit 12 event callback'
    def cb_msg_bit13(self):
        self.message.text = 'bit 13 event callback'
    def cb_msg_bit14(self):
        self.message.text = 'bit 14 event callback'
    def cb_msg_bit15(self):
        self.message.text = 'bit 15 event callback'
    def cb_msg_bit16(self):
        self.message.text = 'bit 16 event callback'


class MainApp(App):
    def build(self):
        return MyGridLayout()

if __name__=="__main__":

    #Config.set('graphics', 'width', '900')
    #Config.set('graphics', 'height', '600')

    def my_callback(dt):
        print 'My callback is called !'

    #Clock.schedule_interval(my_callback,1)
    
    MainApp().run()
