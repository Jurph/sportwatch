#!/usr/bin/python2
import usb.core
import usb.util
import usb.control
import binascii

NIKE_VENDOR_ID = 0x11ac
NIKE_PRODUCT_ID = 0x5455

# 0x0905B310 + zeroes : read-eeprom
# 0x09022908 + zeroes : get-version
# First byte is fixed at 0x09
# Second and third bytes are a mystery
# Fourth byte is OPCODE
#

COMMAND_BYTES = [0x09, 0x05, 0xB3, 0xE2, 0x00, 0x00, 0x00, 0x00,
                 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]

rawCommand = "".join(map(chr, COMMAND_BYTES))


def sendCommand(device, interface, rawCommand):
    while True:
        # Clean outstanding writes waiting on the bus
        try:
            outs = interface[0].read(64, 1000)
            print("Outstanding: ")
            print (outs)
        except:
            break

    print("Writing packet {}").format(binascii.b2a_hex(rawCommand))

    interface[1].write(rawCommand)
    o = open("raw1.OUT", "wb")
    while True:
        try:
            data = interface[0].read(255)[:]
            print(data[:])
            o.write("".join(map(chr, data)))
            nop = interface[0].read(0, 1)[:]
        except:
            break

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
    device.reset()
    sendCommand(device, interface, rawCommand)  # Consider fuzzing this field to see why commands time out
    return 0


if __name__ == "__main__":
    main()

