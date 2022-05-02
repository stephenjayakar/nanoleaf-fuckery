import nanoleafapi
import random
import keyboard
import time


ip = '192.168.4.30'

nl = nanoleafapi.Nanoleaf(ip)
digital_twin = nanoleafapi.NanoleafDigitalTwin(nl)
panels = nl.get_ids()
times = []


while True:
    event = keyboard.read_event()
    if event.event_type == keyboard.KEY_DOWN:
        key = event.name
        # print(f'Pressed: {event}')
        # print(f'Pressed: {event.scan_code}')
        start = time.time()
        # panel_id = random.choice(panels)
        panel_id = panels[event.scan_code % len(panels)]
        panel_id2 = panels[(event.scan_code + 1) % len(panels)]
        panel_id3 = panels[(event.scan_code + 2) % len(panels)]
        digital_twin.set_color(panel_id, (
            random.randint(0, 255),
            random.randint(0, 255),
            random.randint(0, 255),
        ))
        digital_twin.set_color(panel_id2, (
            random.randint(0, 255),
            random.randint(0, 255),
            random.randint(0, 255),
        ))
        digital_twin.set_color(panel_id3, (
            random.randint(0, 255),
            random.randint(0, 255),
            random.randint(0, 255),
        ))

        digital_twin.sync()
        elapsed_time = time.time() - start
        print(f'elapsed time: {elapsed_time}')
        times.append(elapsed_time)
        if key == 'q':
            break

# while True:
#     start = time.time()
#     for panel_id in panels:
#         # set each panel to a random RGB value
#         digital_twin.set_color(panel_id, (
#             random.randint(0,255),
#             random.randint(0,255),
#             random.randint(0,255),
#         ))

#     digital_twin.sync()
#     elapsed_time = time.time() - start
#     print(f'elapsed time: {elapsed_time}')
#     times.append(elapsed_time)
