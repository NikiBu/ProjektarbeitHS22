time2 = 0
distance2 = 0
# trigger = P1
# echo = P2

def on_button_pressed_b():
    global time2, distance2
    time2 = sonar.ping(DigitalPin.P1, DigitalPin.P2, PingUnit.MICRO_SECONDS)
    distance2 = 0.0343 * time2 / 2
    basic.show_number(distance2)
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_forever():
    basic.show_leds("""
        . . . . .
                . . . . .
                . # # # .
                . . . . .
                . . . . .
    """)
basic.forever(on_forever)
