import nanoleafapi
import random
import time


ip = '192.168.4.30'

nl = nanoleafapi.Nanoleaf(ip)
digital_twin = nanoleafapi.NanoleafDigitalTwin(nl)
panels = nl.get_ids()
times = []

while True:
    start = time.time()
    for panel_id in panels:
        # set each panel to a random RGB value
        digital_twin.set_color(panel_id, (
            random.randint(0,255),
            random.randint(0,255),
            random.randint(0,255),
        ))

    digital_twin.sync()
    elapsed_time = time.time() - start
    print(f'elapsed time: {elapsed_time}')
    times.append(elapsed_time)
