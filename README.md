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
- RTC module : HW-084

Run with : uvicorn main:app
## API Reference
### Returns GPIO value
```http
GET /gpio/get/{gpio}
```
| Parameter | Type | Description |
| :-------- | :------- | :------------------------- |
|  `gpio`  |  `int`  |  **Required**. Gpio |
### Set GPIO value
```http
GET /gpio/set/{gpio}/{value}
```
| Parameter | Type | Description |
| :-------- | :------- | :-------------------------------- |
|  `gpio`  |  `int`  |  **Required**. Gpio |
|  `value`  |  `bool`  |  **Required**. GPIO value |

### Engine up or down
```http
POST /engineUpOrDown/set
```
| Parameter | Type | Description |
| :-------- | :------- | :-------------------------------- |
|  `engine`  |  `Engine`  |  **Required**. Engine parameters |

***Engine class*** (all is **Required**)
| Parameter | Type | Description |
| :-------- | :------- | :-------------------------------- |
|  `gpio`  |  `int`  |  Engine run GPIO |
|  `speed`  |  `int`  |  Engine speed |
|  `buttonGpio`  |  `int`  |  Engine run if `buttonGpio` value is true |
|  `limit`  |  `int`  |  Top or bottom limit for engine |
|  `isUp`  |  `bool`  | Engine goes up or down|
|  `isForce`  |  `bool`  |  Ignore `buttonGpio` if `isForce` is true |

### Returns state
```http
GET /state/get
```
### Set state
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
|  `dateTime `  |  `DateTime`  |  Date and time|

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
