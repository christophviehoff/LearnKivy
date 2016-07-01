import kivy
from kivy.app import App

kivy.require('1.9.0')

import platform
# setup initial screen size at start
# from kivy.config import Config
# Config.set('graphics', 'width', '970')
# Config.set('graphics', 'height', '728')
from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from time import sleep

'''
#arduino communication
import pyfirmata
board = pyfirmata.Arduino('COM20')

#start an iterator thread so
#serial buffer doesn't overflow
iter8 = pyfirmata.util.Iterator(board)
iter8.start()

#set up pin D9 and 10 as Servo Output
pin9 = board.get_pin('d:9:s')
pin10 = board.get_pin('d:10:s')
'''
#arduino servo commands
def move_servo1(a):
    pin9.write(a)
    print('talking to servo 1')

def move_servo2(a):
    pin10.write(a)
    print('talking to servo 2')


HomePos=90

# color definitions
green = 0, 1, 0, 1
white = 1, 1, 1, 1


class ServoControlScreen(BoxLayout):
    # py to kv object mapping for objects we
    # want to manipulate
    slider1 = ObjectProperty(None)
    slider2 = ObjectProperty(None)
    sw_enable = ObjectProperty(None)
    pb1_eject = ObjectProperty(None)
    pb2_eject = ObjectProperty(None)
    pb1_reset = ObjectProperty(None)
    pb2_reset = ObjectProperty(None)
    message = ObjectProperty(None)

    def cb_info(self):
        self.message.text = ('Developed with kivy version {} and Python {}\n'
                             'Revision 0.1 - Author: Christoph Viehoff'.
                             format(kivy.__version__, platform.python_version()))

    def cb_update_slider1(self):
        move_servo1(self.slider1.value)
        print('Servo 1 just got updated')
        print('Servo 1 value is now {:.2f}'.format(self.slider1.value))

    def cb_update_slider2(self):
        move_servo2(self.slider2.value)
        print('Servo 2 just got updated')
        print('Servo 2 value is now {:.2f}'.format(self.slider2.value))

    def cb_enable(self):
        print('My enable state is now {}'.format(self.sw_enable.active))
        # enable = True, disable = False
        if not self.sw_enable.active:
            self.pb1_eject.disabled = True
            self.pb2_eject.disabled = True
            self.pb1_reset.disabled = True
            self.pb2_reset.disabled = True
            self.slider1.disabled = True
            self.slider2.disabled = True
        else:
            self.pb1_eject.disabled = False
            self.pb2_eject.disabled = False
            self.pb1_reset.disabled = False
            self.pb2_reset.disabled = False
            self.slider1.disabled = False
            self.slider2.disabled = False

    def cb_servo1_eject(self):
        move_servo1(self.slider1.value)
        print('Servo 1 just got ejected.')
        # move_servo1(self.slider1.value)

    def cb_servo2_eject(self):

        move_servo2(self.slider2.value)
        print('Servo 2 just got ejected.')
        # move_servo2(self.slider2.value)

    def cb_servo1_reset(self):
        move_servo1(HomePos)
        print('Servo 1 just got reset.')
        #self.slider1.value = HomePos

    def cb_servo2_reset(self):
        move_servo2(HomePos)
        print('Servo 2 just got reset.')
        #self.slider2.value = HomePos


class servoGui(App):
    pass


if __name__ == '__main__':
    servoGui().run()
