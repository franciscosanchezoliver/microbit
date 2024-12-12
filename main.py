def on_button_pressed_a():
    for index in range(1):
        music.play(music.string_playable("- E E - E - - - ", 120),
            music.PlaybackMode.UNTIL_DONE)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_gesture_shake():
    basic.clear_screen()
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

def on_button_pressed_b():
    basic.show_icon(IconNames.HEART)
input.on_button_pressed(Button.B, on_button_pressed_b)

basic.show_string("Caution!")

def on_forever():
    pass
basic.forever(on_forever)
