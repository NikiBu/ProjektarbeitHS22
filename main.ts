let time2 = 0
let distance2 = 0
//  trigger = P1
//  echo = P2
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    
    time2 = sonar.ping(DigitalPin.P1, DigitalPin.P2, PingUnit.MicroSeconds)
    distance2 = 0.0343 * time2 / 2
    basic.showNumber(distance2)
})
basic.forever(function on_forever() {
    basic.showLeds(`
        . . . . .
                . . . . .
                . # # # .
                . . . . .
                . . . . .
    `)
})
