from microbit import *
endtime = 0
while True:
    endtime += 1
    display.scroll(str(endtime), delay=111)
    if button_a.is_pressed():
        break
display.scroll(str(endtime), delay=200)
display.clear()
