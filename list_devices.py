# can_list_devices.py

import canlib

for dev in canlib.connected_devices():
	print(dev.probe_info())
