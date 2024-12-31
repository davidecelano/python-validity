from proto9x.usb import usb
from proto9x.sensor import factory_reset

usb.enable_trace()
usb.open()
factory_reset()
usb.disable_trace()
