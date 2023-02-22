 
Init my GPIO with :
- 17 --> Button for up
- 27 --> Button for down
- 13 --> Engine run
- 19 --> Engine direction
- 26 --> Engine stop

My hardware :
- Engine reference : 23HS22-2804S
- step driver reference : DM556 (5.6A (2.8*2), Half Current, 20000 pulse/rev)
- RTC module : HW-084
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
|  `isUp`  |  `int`  | Engine goes up or down|
|  `isForce`  |  `int`  |  Ignore gpio button if `isForce` is true |

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
|  `dateTimeWithDayOfWeek`  |  `DateTimeWithDayOfWeek`  |  Date, time and day of week |

***DateTimeWithDayOfWeek class*** (all is **Required**)
| Parameter | Type | Description |
| :-------- | :------- | :-------------------------------- |
|  `date`  |  `str`  |  Date (format : dd/MM/yyyy) |
|  `time`  |  `str`  |  Time (format : hh:mm) |
|  `dayOfWeek`  |  `int`  |  Day of week|
