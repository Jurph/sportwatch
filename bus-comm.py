import usb.core
import usb.util
import sys
 
# Find Device
def detach_kernel_driver(self, dev_handle, intf):
    _check(_lib.usb_detach_kernel_driver_np(dev_handle, intf))
        
device = usb.core.find(idVendor=0x11ac, idProduct=0x5455)

# replace  <idVendor> and <idProduct> with what lsusb -v returned
# in my case we have a Vendor ID of 0x11AC (Nike) and a product 0x5455
# Right rear USB port appears to be Bus 003 / Device 004 at the moment.

if device is None:
    raise ValueError('Device not found')
for self in range(10):
    try:
        device.set_configuration(self)
    except:
        pass

# This enumerates all of the valid bmRequests between 1 and 200
for bmRequest in range(200):
    try:
        #ctrl_transfer( bmRequestType, bmRequest, wValue, wIndex, nBytes)
        usbCom = device.ctrl_transfer(0xc0, bmRequest, 0, 0, 1)
        print usbCom
    except:
        pass
