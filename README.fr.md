[![en](https://img.shields.io/badge/lang-en-ab4b52.svg)](https://github.com/tlebigre/henHouseBoardBackendApi/blob/main/README.md)
[![fr](https://img.shields.io/badge/lang-fr-318ce7.svg)](https://github.com/tlebigre/henHouseBoardBackendApi/blob/main/README.fr.md)

Initialisation de mes GPIO :
- 17 --> Bouton pour monter
- 27 --> Bouton pour descendre
- 13 --> Le moteur fonctionne
- 19 --> Direction du moteur
- 26 --> Arret du moteur

Mon matériel :
- Référence du moteur : 23HS22-2804S
- Référence du driver : DM556 (5.6A (2.8*2), Half Current, 20000 pulse/rev)
- Module RTC : HW-084

## Générer les fichiers grpc

```bash
pip install grpcio
```

```bash
pip install grpcio-tools
```

```bash
python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. board.proto
```

## Développement

Démarrer le serveur de développement :

```bash
python server.py
```
