input.onButtonPressed(Button.A, function on_button_pressed_a() {
    for (let index = 0; index < 1; index++) {
        music.play(music.stringPlayable("- E E - E - - - ", 120), music.PlaybackMode.UntilDone)
    }
})
input.onGesture(Gesture.Shake, function on_gesture_shake() {
    basic.clearScreen()
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    basic.showIcon(IconNames.Heart)
})
basic.showString("Caution!")
basic.forever(function on_forever() {
    
})
