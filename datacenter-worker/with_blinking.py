#!/usr/bin/env python3

from sys import argv, exit
import subprocess

from led_indicator import LedIndicator

li = LedIndicator()

def run_subprocess():
    process = subprocess.Popen(' '.join(argv[1:]), shell=True, stdout=subprocess.PIPE)
    out, err = process.communicate()
    errcode = process.returncode
    return out, err, errcode

out, err, errcode = li.with_blinking_do('red', run_subprocess)
exit(errcode)
