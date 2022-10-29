#!/bin/bash

set -e

echo 'PATH=$PATH:$HOME/bcgplatinion-15-million-kelvin/datacenter-worker/
# Simple autostart
TMUX_PROCESS="$(pgrep tmux)"
if [[ -z "$TMUX_PROCESS" ]]; then
  tmux new-session "leds_off.py && /home/admin/bcgplatinion-15-million-kelvin/datacenter-worker/main.py" \; detach
fi
' >> $HOME/.bashrc
sudo apt install -y python3-rpi.gpio
sudo pip3 install requests
