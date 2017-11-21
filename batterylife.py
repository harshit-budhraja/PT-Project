#!/usr/bin/env python2.7

# dbus-send --print-reply --system --dest=org.freedesktop.UPower /org/freedesktop/UPower/devices/battery_BAT0 org.freedesktop.DBus.Properties.Get string:org.freedesktop.UPower.Device string:'Percentage'

import dbus

bus = dbus.SystemBus()
bat0_object = bus.get_object('org.freedesktop.UPower', 
                      '/org/freedesktop/UPower/devices/battery_BAT0')
bat0 = dbus.Interface(bat0_object, 'org.freedesktop.DBus.Properties')

print bat0.Get("org.freedesktop.UPower.Device", "Percentage")

