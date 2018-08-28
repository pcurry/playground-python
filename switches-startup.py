from digitalio import DigitalInOut, Direction, Pull
import board
import time
 
led = DigitalInOut(board.D13)
led.direction = Direction.OUTPUT

def button_init(button, pull=Pull.DOWN):
    button_obj = DigitalInOut(button)  
    button_obj.direction = Direction.INPUT
    button_obj.pull = pull
    return button_obj

button_a = button_init(board.BUTTON_A)
button_b = button_init(board.BUTTON_B)
slide_button = button_init(board.SLIDE_SWITCH, pull=Pull.UP)
 
while True:
    if (not slide_button.value) and (button_a.value or button_b.value): # Light if either button pushed, disabled by slide_button
        led.value = True
    else:
        led.value = False
 
    time.sleep(0.01)