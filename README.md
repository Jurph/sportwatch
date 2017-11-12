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
- Try sending some traditional read/write commands to get more config info