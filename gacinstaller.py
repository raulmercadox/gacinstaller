# -*- coding: utf-8 -*-
"""
Created on Sat Sep  7 12:08:39 2019

@author: ezmerra
"""

import sys
import os
import glob
import ntpath

OUTPUTFILE = "gacinstaller.bat"
BASEFOLDER = "c:\\etelcrmcode"

def main():
    #usage: $ python generatepsbbat.py <folder>
    if not len(sys.argv) == 2:
        print("Usage: python gacinstaller.py <folder>")
        sys.exit(-1)
    
    folder = sys.argv[1]
    if not os.path.exists(folder):
        print("The folder " + folder + " does not exist")
        sys.exit(1)

    ntpath.basename(sys.argv[1])
    files = glob.glob(os.path.join(folder, "*.dll"))
    process_files(files)
    print("The file " + os.path.join(BASEFOLDER, OUTPUTFILE) + " was generated.")

    sys.exit(0)

def process_files(files):
    if os.path.isfile(os.path.join(BASEFOLDER, OUTPUTFILE)):
        os.remove(os.path.join(BASEFOLDER, OUTPUTFILE))
        
    with open(os.path.join(BASEFOLDER, OUTPUTFILE), "a") as myfile:
        myfile.write('iisreset /stop\n')
        for file in files:
            onlyname = pathleaf(file)
            myfile.write('c:\\etelcrmcode\\gacutil.exe /i c:\\etelcrmcode\\' + onlyname +'\n')
        myfile.write('iisreset /start\n')

def pathleaf(path):
    head, tail = ntpath.split(path)
    return tail or ntpath.basename(head)            

if __name__ == "__main__":
    main()
