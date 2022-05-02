import nanoleafapi
import random
import time


ip = '192.168.4.30'

nl = nanoleafapi.Nanoleaf(ip)
digital_twin = nanoleafapi.NanoleafDigitalTwin(nl)
panels = nl.get_ids()

while True:
    for panel_id in panels:
        start = time.time()
        # set each panel to a random RGB value
        digital_twin.set_color(panel_id, (
            random.randint(0,255),
            random.randint(0,255),
            random.randint(0,255),
        ))
        end = time.time() - start

    digital_twin.sync()
