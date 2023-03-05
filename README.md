# MicroPython

## Installation
```bash
pip install mpremote
```
## How to run
```bash
mpremote run leds.py
```
## In case Permisson denied try:
```bash
mpremote --help
mpremote u0
sudo usermod --append --group dialout $(whoami)
su - $(whoami)
mpremote u0
mpremote u0 run leds.py
```
