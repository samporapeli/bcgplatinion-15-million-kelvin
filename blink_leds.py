#!/usr/bin/env python3

from time import sleep
from led_indicator import LedIndicator

li = LedIndicator()
li.light_led('green', 0.5)
li.light_led('yellow', 0.3)
for i in range(10):
    li.light_led('red', 0.2)
    sleep(0.1)
li.light_led('yellow', 0.3)
li.light_led('green', 0.5)
