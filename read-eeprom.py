#!/usr/bin/python2
NIKE_VENDOR_ID = 0x11ac
NIKE_PRODUCT_ID = 0x5455

import time
import usb.core
import usb.util
import usb.control

device = usb.core.find(idVendor=NIKE_VENDOR_ID, idProduct=NIKE_PRODUCT_ID)
device.reset()
if device.is_kernel_driver_active(0):
    print("Detaching kernel driver\n")
    device.detach_kernel_driver(0)

configuration = usb.util.find_descriptor(device, bConfigurationValue=1)
interface = configuration[(0, 0)]

#  This is a packet that reads data out of the EEPROM on board.
bytes_num = [0x09, 0x05, 0xb3, 0x10, 0x00, 0x00, 0x00, 0x00,
             0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
             0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
             0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
             0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
             0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
             0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
             0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]
data_raw = "".join(map(chr, bytes_num))

while True:
    # Clean outstanding
    try:
        outs = interface[0].read(64)
        print("Outstanding: ")
        print (outs)
    except:
        break

print("Writing packet ")

interface[1].write(data_raw)
o = open("raw1.OUT", "wb")


while True:
    data = interface[0].read(64)[:]
    print(data[:])
    o.write("".join(map(chr, data)))
    nop = interface[0].read(0)[:]


    # usb.util.dispose_resources(device)