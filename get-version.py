#!/ usr / bin /python2
NIKE_VENDOR_ID = 0x11ac
NIKE_PRODUCT_ID = 0x5455

import usb.core
import usb.util
import usb.control

dev = usb.core.find(idVendor=NIKE_VENDOR_ID,  idProduct=NIKE_PRODUCT_ID)

if dev.is_kernel_driver_active(0):
    print("Detaching kernel driver\n")
    dev.detach_kernel_driver(0)

configuration = usb.util.find_descriptor(dev, bConfigurationValue=1)
interface = configuration[(0, 0)]

#  This is a large constant byte array that comprises the GetVersion command
bytes_num = [0x09, 0x02, 0x29, 0x08, 0x00, 0x00, 0x00, 0x00,
             0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
             0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
             0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
             0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
             0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
             0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
             0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00 ]

data_raw = "" .join(map(chr, bytes_num))
interface[1].write(data_raw)
version = interface[0].read(64)
letter = chr(version[3])

code = version[5] << 8 + version[4]

print ("Version : %s%d"%(letter, code ))

# With this code python will replay the packet to obtain a version number, and
# will print what our analysis shows is the version from the response. The byte at
# offset 3 an ASCII character, and 4 and 5 a big-endian 16Bit integer

