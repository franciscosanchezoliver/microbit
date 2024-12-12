def on_button_pressed_a():
    global counter
    counter = counter + -1
    if counter < 0:
        basic.show_string("NO")
        counter = 0
    else:
        basic.show_string("" + str(counter))
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_gesture_shake():
    basic.clear_screen()
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

def on_button_pressed_b():
    global counter
    counter = counter + 1
    basic.show_string("" + str(counter))
input.on_button_pressed(Button.B, on_button_pressed_b)

counter = 0
basic.show_string("" + str(counter))
counter = 0