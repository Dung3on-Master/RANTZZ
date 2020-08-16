import time
from tkinter import *

import scanner
import filemover
import fullscan
import SpesificFileScan


def rantsstart():

   master = Tk()
   
   Label(master, text="Rantzz Security").grid(row=0, sticky=W)

   Button(master, text='Full Scan', command=fullscan.fullscanstart).grid(row=1, sticky=W, pady=4)

   Button(master, text='Selective Scan', command=scanner.scanstart).grid(row=2, sticky=W, pady=4)

   Button(master, text='File Scan', command=SpesificFileScan.spesificscanstart).grid(row=3, sticky=W, pady=4)

   Button(master, text='Move To Secure Folder', command=filemover.movetosurcurefolder).grid(row=4, sticky=W, pady=4)

   Button(master, text='Quit', command=master.quit).grid(row=6, sticky=W, pady=4)
   
   time.sleep(1)
   print("log waiting for input")

   mainloop()

if __name__ == "__main__":
    rantsstart()


