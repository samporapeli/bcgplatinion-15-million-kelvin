#!/usr/bin/env python3

import RPi.GPIO as GPIO
from time import sleep, time
from multiprocessing import Process

BLINK_OFF_TIME = 0.15
BLINK_ON_TIME = 0.4

class LedIndicator:
    def __init__(self): 
        self.GREEN = 8
        self.YELLOW = 10
        self.RED = 12

        self.color_to_led = {
            'green': self.GREEN,
            'yellow': self.YELLOW,
            'red': self.RED,
        }

        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.GREEN, GPIO.OUT, initial=GPIO.LOW)
        GPIO.setup(self.YELLOW, GPIO.OUT, initial=GPIO.LOW)
        GPIO.setup(self.RED, GPIO.OUT, initial=GPIO.LOW)

    def led_on(self, color):
        GPIO.output(self.color_to_led[color], GPIO.HIGH)

    def led_off(self, color):
        GPIO.output(self.color_to_led[color], GPIO.LOW)

    def leds_off(self):
        for color in self.color_to_led.keys():
            self.led_off(color)

    def light_led(self, color, time=0):
        self.led_on(color)
        sleep(time)
        if time > 0:
            self.led_off(color)

    def blink(self, color, on_time=BLINK_ON_TIME, off_time=BLINK_OFF_TIME):
        while True:
            self.led_on(color)
            sleep(on_time)
            self.led_off(color)
            sleep(off_time)

    def with_led_do(self, color, task):
        self.led_on(color)
        return_value = task()
        self.led_off(color)
        return return_value

    def with_blinking_do(self, color, task, on_time=BLINK_ON_TIME, off_time=BLINK_OFF_TIME):
        blinking = Process(target=self.blink, args=(color,))
        blinking.start()
        return_value = task()
        blinking.kill()
        self.led_off(color)
        return return_value
