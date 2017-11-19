# Overview

This project is based on the excellent inroads made by the Dutch university students who wrote
this paper (https://www.os3.nl/_media/2013-2014/courses/ccf/smartwatches-hristo-leendert.pdf) and I'm
grateful to them for their work.  My goal is to replicate their results on my own Nike+ Smartwatch
and then begin reading more aggressively from the watch.  It's possible that this will fail horribly.

# Sources

PDF is included in this repo for those who want to play along at home.  **get-version.py** and **read-eeprom.py** are copied directly from the paper. Also thanks to the author of http://dan3lmi.blogspot.com/2012/10/sniffing-usb-traffic-different.html for
**bus-comm.py** and information on using the **lsusb** command in linux.

# Skeletons

I've forgotten where I encountered the idea of keeping a skeletons file, but here is some technical debt/TODO list for this project.

- A great deal of the Dutch code is duplicated between routines. Refactor this into **initialize.py**, pass in the ID strings, get back an addressable object
- Set up static byte arrays with the known commands in them
- Try sending some traditional read/write commands to get more config info (bus-comm.py does this but doesn't cleanly produce output)

## Commands to try

- 0x09: **upgrade firmware** - just hand it some binary, apparently (?!)
- 0x12: **eeprom query** - can also include a 24-bit address where the workout is stored
- 0x13: **battery query** -
- 0x14: **read desktop data block** - not clear what the "desktop data block" is
- 0x15: **write DDB** - hmmm
- 0x36: **write gender** - n.b. gender is a string() not an int() - this is the future liberals want!
- 0x41: **write Attaboy** - this probably adds motivational phrases to the post-run data, probably vulnerable to malformed inputs
- 0x51: **ephemeris query** - potential
- 0xE4: **test GPS** - 0xE4, test. ID (1-4), sat_number (1-24, optional), duration (seconds)
- 0xE7: **test-buzzer** - (1=play tone, 0= stop), freq. in Hz, duration in ms (chiptune time!)
- 0xEB: **test-accel** - (1 = sample accelerometer, 0 = stop), no info on what data it returns



