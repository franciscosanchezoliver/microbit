input.onButtonPressed(Button.A, function () {
    counter = counter + -1
    if (counter < 0) {
        basic.showString("NO")
        counter = 0
    } else {
        basic.showString("" + counter)
    }
})
input.onGesture(Gesture.Shake, function () {
    basic.clearScreen()
})
input.onButtonPressed(Button.B, function () {
    counter = counter + 1
    basic.showString("" + counter)
})
let counter = 0
basic.showString("" + counter)
counter = 0
