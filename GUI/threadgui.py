'''
Created on Mar 7, 2017

@author: dpascualhe

Threading camera class

Based on @nuriaoyaga code:
https://github.com/RoboticsURJC-students/2016-tfg-nuria-oyaga/blob/master/gui/threadgui.py
'''

import threading
import time
from datetime import datetime

t_cycle = 70 # ms

class ThreadGUI(threading.Thread):

    def __init__(self, gui):
        
        self.gui = gui
        threading.Thread.__init__(self)

    def run(self):
        while(True):
            start_time = datetime.now()
            self.gui.updGUI.emit()
            end_time = datetime.now()
            dt = end_time - start_time
            dtms = ((dt.days * 24 * 60 * 60 + dt.seconds) * 1000
                + dt.microseconds / 1000.0)

            if(dtms < t_cycle):
                time.sleep((t_cycle - dtms) / 1000.0);