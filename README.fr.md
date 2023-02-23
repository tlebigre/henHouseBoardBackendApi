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
## API Reference
### Retourne la valeur du GPIO
```http
GET /gpio/get/{gpio}
```
| Parameter | Type | Description |
| :-------- | :------- | :------------------------- |
|  `gpio`  |  `int`  |  **Requis**. Gpio |
### Donne la valeur au GPIO
```http
GET /gpio/set/{gpio}/{value}
```
| Parameter | Type | Description |
| :-------- | :------- | :-------------------------------- |
|  `gpio`  |  `int`  |  **Requis**. Gpio |
|  `value`  |  `bool`  |  **Requis**. Valeur du Gpio |

### Le moteur monte ou descend
```http
POST /engineUpOrDown/set
```
| Parameter | Type | Description |
| :-------- | :------- | :-------------------------------- |
|  `engine`  |  `Engine`  |  **Requis**. Paramètres du moteur |

***Engine class*** (all is **Required**)
| Parameter | Type | Description |
| :-------- | :------- | :-------------------------------- |
|  `gpio`  |  `int`  |  Gpio de fonctionnement du moteur |
|  `speed`  |  `int`  |  Vitesse du moteur |
|  `buttonGpio`  |  `int`  |  Le moteur fonctionne si la valeur de `buttonGpio` est vrai |
|  `limit`  |  `int`  |  Limite haute ou basse du moteur |
|  `isUp`  |  `bool`  | Le moteur monte ou descend|
|  `isForce`  |  `bool`  |  Ignore `buttonGpio` si `isForce` est vrai |

### Returns state value
```http
GET /state/get
```
### Set state value
```http
GET /state/set/{state}
```
| Parameter | Type | Description |
| :-------- | :------- | :------------------------- |
|  `state`  |  `int`  |  **Required**. State value|

### Returns date time value
```http
GET /dateTime/get
```
| Parameter | Type | Description |
| :-------- | :------- | :-------------------------------- |
|  `dateTime `  |  `DateTime`  |  **Required**. Date and time|

***DateTime class*** 
| Parameter | Type | Description |
| :-------- | :------- | :-------------------------------- |
|  `date`  |  `str`  |  Date (format : dd/MM/yyyy) |
|  `time`  |  `str`  |  Time (format : hh:mm) |
### Set date time value
```http
POST /dateTime/set
```
| Parameter | Type | Description |
| :-------- | :------- | :-------------------------------- |
|  `dateTimeWithDayOfWeek`  |  `DateTimeWithDayOfWeek`  |  **Required**. Date, time and day of week |

***DateTimeWithDayOfWeek class*** (all is **Required**)
| Parameter | Type | Description |
| :-------- | :------- | :-------------------------------- |
|  `date`  |  `str`  |  Date (format : dd/MM/yyyy) |
|  `time`  |  `str`  |  Time (format : hh:mm) |
|  `dayOfWeek`  |  `int`  |  Day of week|
