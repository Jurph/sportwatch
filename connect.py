#!/usr/bin/python2
NIKE_VENDOR_ID = 0x11ac
NIKE_PRODUCT_ID = 0x5455

import time
import usb.core
import usb.util
import usb.control


def connect(Vendor_ID, Product_ID):
    device = usb.core.find(idVendor=Vendor_ID, idProduct=Product_ID)
    device.reset()
    if device.is_kernel_driver_active(0):
        print("Detaching kernel driver\n")
        device.detach_kernel_driver(0)

    configuration = usb.util.find_descriptor(device, bConfigurationValue=1)
    interface = configuration[(0, 0)]
    return device, interface

def main():
    device, interface = connect(NIKE_VENDOR_ID, NIKE_PRODUCT_ID)
    print "Found device: {}".format(str(device))
    print "Found interface: {}".format(str(interface))
    return 0

if __name__ == "__main__":
    main()

