# Overview

This project is based on the excellent inroads made by the Dutch university students who wrote
this paper (https://www.os3.nl/_media/2013-2014/courses/ccf/smartwatches-hristo-leendert.pdf) and I'm
grateful to them for their work.  My goal is to replicate their results on my own Nike+ Smartwatch
and then begin reading more aggressively from the watch.  It's possible that this will fail horribly.

# The Problem

While the Dutch paper is excellent about documenting the work they did capturing traffic and performing replay attacks,
they did not venture into reverse engineering the packet format.  So while I have a tantalizing set of opcodes I can send
using trial and error (see below), there is no explanation of why (e.g.) opcode **0x10** must be transmitted as **0x0905B310**.
This means that when I try to send a fun opcode below, my fun is greatly curtailed by having to rely on static values in the
first few bytes I send.

## The first byte

Is always fixed at **0x09** in the Dutch paper, but seems to work well set to 0x08 as well.  Probably worth exploring some other values
for this field.

## The second byte

The 2d byte seems to depend on the opcode you're sending.  For 0xE7 (test buzzer) a value of 0x01 returns nothing, and a few other
low values (0x02 - 0x08) the device returns an array that includes the third byte in the return data.

## The third byte

The 3rd byte is returned in an array with "1, 2, [third_byte], lots of zeroes, [third byte]."

## The fourth byte

...is the opcode.  It's possible that 2nd and 3rd byte together form a lazy 24-bit address (disregarding some other item) and
are executing some sort of read action.



# Sources

PDF is included in this repo for those who want to play along at home.  **get-version.py** and **read-eeprom.py** are copied directly from the paper. Also thanks to the author of http://dan3lmi.blogspot.com/2012/10/sniffing-usb-traffic-different.html for
**bus-comm.py** and information on using the **lsusb** command in linux.

# Skeletons

I've forgotten where I encountered the idea of keeping a skeletons file, but here is some technical debt/TODO list for this project.

- A great deal of the Dutch code is duplicated between routines. Refactor this into **initialize.py**, pass in the ID strings, get back an addressable object
- Set up static byte arrays with the known commands in them
- Try sending some traditional read/write commands to get more config info

## Interesting OPCODEs

Here are some interesting commands I found in the *commands.xml* appendix...

- 0x03 - **Latchup** - lock battery
- 0x04 - **bootblock** - Go to boot block
- 0x05 - **console-write** - wonder what this writes to?
- 0x09 - **upgrade** - takes a binary file as an argument
- 0x10 - **eeprom-read** - reads from the eeprom, takes a 24-bit address for workout storage
- 0x10 - **eeprom-query** - get total bytes of available storage
- 0x14 - **desktop-read**
- 0x15 - **desktop-write** - not clear why I want to read/write the desktop data block, but I'm in.
- 0x26 - **flags-sync** - probably holds stateful flags
- 0x36 - **option-gender** - pass a string (not a BOOL or INT!) to this field
- 0x41 - **write-attaboy** - probably adds a string to the motivational post-workout 'attaboys'
- 0x51 - **ephemeris-query** - get ephemerides info (may have satIDs)
- 0x53 - **gpspatch-query** - reads patch level of GPS firmware
- 0x54 - **gpspatch-update** - takes a binary, presumably GPS modem firmware! Oooooo...
- 0xE4 - **test-gps** - (test no 1-4, satellite ID, and duration)
- 0xE7 - **test-buzzer** - (1 = play, 0 = stop) ; (frequency in Hz, optional) ; (duration in ms, optional)
- 0xEB - **test-accel** - 1 = sample accelerometer, 0 = exit test