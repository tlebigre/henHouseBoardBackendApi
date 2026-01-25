[![en](https://img.shields.io/badge/lang-en-ab4b52.svg)](https://github.com/tlebigre/henHouseBoardBackendApi/blob/main/README.md)
[![fr](https://img.shields.io/badge/lang-fr-318ce7.svg)](https://github.com/tlebigre/henHouseBoardBackendApi/blob/main/README.fr.md)

Initialisation de mes GPIO :
- 17 --> Bouton pour monter
- 27 --> Bouton pour descendre
- 13 --> Le moteur fonctionne
- 19 --> Direction du moteur
- 26 --> Arret du moteur
- 18 --> Détection de l'alimentation secteur

Mon matériel :
- Référence du moteur : 23HS22-2804S
- Référence du driver : DM556 (5.6A (2.8*2), Half Current, 20000 pulse/rev)
- Module RTC : HW-084
- Raspberry PI 3
- Mini UPS Battery Backup : Model FX-5V, Capacity 10000mAh
- DollaTek AC 220V microcontrôleur niveau TTL module d'isolation optocoupleur

## Développement

Démarrer le serveur de développement :

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