#!/usb/bin/env python3

import debinterface
 
print(dir(interfaces))

adapters = debinterface.interfaces()

for adapter in adapters:
    item = adapter.export()
    print(item['name'])
