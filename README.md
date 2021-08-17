# TRaffic Lights

This short bit of code serves the following purposes:

- Illustrating the idea classes and inheritance
- Illustrating the use of methods
- Illustrating the use of instance variables

## Requirements

This code requires either:

- Raspberry Pi + SenseHAT, or
- SenseHAT simulator (https://trinket.io/sense-hat), or
- Raspberry Pi Simulator + SenseHAT simulator ()
- Raspberry Pi + SenseHAT simulator ()

### Pi & SenseHAT (Physical hardware)

Docs: [...](#)

A Raspberry PI with a SenseHAT will need to have the SenseHAT support files installed:
```shell
sudo apt-get update
sudo apt-get install sense-hat
sudo pip3 install pillow
```

### SenseHAT simulator (Runs on Web)

Docs: [https://sense-emu.readthedocs.io](https://sense-emu.readthedocs.io)

You will need to create a `main.py` and a `TrafficLight.py` file and put the required code into the respective files.

### Raspberry Pi (Physical) and SenseHAT Emulator
Docs: [https://sense-emu.readthedocs.io](https://sense-emu.readthedocs.io)

If you wish to run the SenseHAT emulator on the Raspberry Pi, then you will need to do the following:

- Install the emulator
```shell
sudo apt-get update
sudo apt-get install python-sense-emu python3-sense-emu sense-emu-tools
```

Any references to `sense_hat` will be replaced by `sense_emu`. For example:
```python
from sense_emu import SenseHat
```

### Raspberry PI and SenseHAT simulator (Both emulated) 

*Details to come...*
Docs: [...](#)
