[![en](https://img.shields.io/badge/lang-en-ab4b52.svg)](https://github.com/tlebigre/henHouseBoardBackendApi/blob/main/README.md)
[![fr](https://img.shields.io/badge/lang-fr-318ce7.svg)](https://github.com/tlebigre/henHouseBoardBackendApi/blob/main/README.fr.md)

Init my GPIO with :
- 17 --> Button for up
- 27 --> Button for down
- 13 --> Engine run
- 19 --> Engine direction
- 26 --> Engine stop

My hardware :
- Engine reference : 23HS22-2804S
- Step driver reference : DM556 (5.6A (2.8*2), Half Current, 20000 pulse/rev)

## Generate grpc files

```bash
pip install grpcio
```

```bash
pip install grpcio-tools
```

```bash
python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. board.proto
```

## Developing

## /etc/systemd/system/henhouse-board.service
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
