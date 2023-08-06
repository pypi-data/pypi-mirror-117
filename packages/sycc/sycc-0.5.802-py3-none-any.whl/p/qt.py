from sys import path
path.append('..')
from p.__init__ import *
from e.__init__ import *
import platform
os=platform.system()
pai2='π'
qt_font='\033[1;33m球体\033[0m\033[1;1m'
#公式
'''
S=4πR²
V=4/3πR³
'''
def part_qt():
    print('球体-β')
    while True:
        try:
            r=eval(r=input('请输入半径'))
            if r<=0:
        	    print('你输入的数太小\n请重新选择'+qt_font+'模式重试')
        	    switch(3)
        	    break
        except ZeroDivisionError:
            print('除数不能为0')
        except Exception:
            print('请输入有效数字')
            break