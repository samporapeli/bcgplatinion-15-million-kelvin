#!/usr/bin/env python3

import requests
import subprocess
from time import sleep

from led_indicator import LedIndicator

li = LedIndicator()

config = {
#        'endpoint': 'http://ec2-3-68-221-30.eu-central-1.compute.amazonaws.com:3333/api/v1',
    'endpoint': 'http://sampo.website:3333/api/v1',
    'rpi_id': 1,
}

while True:
    try:
        li.leds_off()
        li.led_on('green')
        work_request_fun = lambda: requests.post(f'{config["endpoint"]}/request_work', json={
            'rpi_id': config['rpi_id'],
        })
        li.leds_off()
        work_request = li.with_blinking_do('yellow', work_request_fun, 0.05, 0.05)
        work_task = work_request.json()['shell_command']
        if work_task:
            print(f'got work: {work_task}')
            def run_work_task():
                process = subprocess.Popen(work_task, shell=True, stdout=subprocess.PIPE)
                out, err = process.communicate()
                errcode = process.returncode
                return out, err, errcode
            out, err, errcode = li.with_blinking_do('red', run_work_task)
            work_response_fun = lambda: requests.post(f'{config["endpoint"]}/request_work', json={
                'rpi_id': config['rpi_id'],
                'work_response': out,
                'exit_status': errcode,
            })
            li.with_blinking_do('yellow', work_response_fun, 0.05, 0.05)
            li.leds_off()
            li.led_on('green')
            sleep(1)
        else:
            sleep(1)
    except requests.exceptions.ConnectionError:
        print('Connection error')
        sleep(1)