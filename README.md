[![en](https://img.shields.io/badge/lang-en-ab4b52.svg)](https://github.com/tlebigre/henHouseBoardBackendApi/blob/main/README.md)
[![fr](https://img.shields.io/badge/lang-fr-318ce7.svg)](https://github.com/tlebigre/henHouseBoardBackendApi/blob/main/README.fr.md)

Init my GPIO with :
- 17 --> Button for up
- 27 --> Button for down
- 13 --> Engine run
- 19 --> Engine direction
- 26 --> Engine stop
- 18 --> AC power detection

My hardware :
- Engine reference : 23HS22-2804S
- Step driver reference : DM556 (5.6A (2.8*2), Half Current, 20000 pulse/rev)
- Raspberry PI 3
- Mini UPS Battery Backup : Model FX-5V, Capacity 10000mAh
- DollaTek AC 220V Optocoupler Isolation Module – 1-Channel TTL Level Tester For PLC & Microcontrollers

## Developing

Start a development server:

```bash
python main.py
```

## /etc/systemd/system/henhouse-board.service
```bash
[Unit]
Description=HenHouse Board Backend
After=network.target

[Service]
Type=simple
User=lebigre
WorkingDirectory=/opt/henhouse/board
Environment=PYTHONPATH=/opt/henhouse/board
Environment=HARDWARE_MODE=raspberry
ExecStart=/opt/henhouse/board/venv/bin/python /opt/henhouse/board/main.py
Restart=always
RestartSec=5

[Install]
WantedBy=multi-user.target
```
