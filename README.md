# Jade client API guide #

This document explains how to connect to and control Jade systems using JSON requests over sockets. 
## Client Requirements: ##
**Operating System:** Linux, Windows


## Connection Steps ##
1. Connect your client device to the Jade system using ethernet cable
2. Set your client device static IP address to **192.168.42.2**
3. Create a websocket client and connect it to the IP address **192.168.42.1** and port no **4040**
4. Create a `JSON` request and send it as a string through the opened `websocket-client`


## JSON Request Structure ##
JSON request contains two fields `commandId` and `value` (case sensitive). The field `commandId` id is of type integer and the field `value` is of type string. `commandId` is a required field and must be present on all the request data. `value` is not required for some of the commands (Please see the JSON requests list). 

An example request:
```javascript
{
  "commandId": 1001,
  "value": ""
 }
 ```

## Example Code ##
[This is an example code](./command_websocket.py) to create a `websocket-client` to port no **4040** at IP address **192.168.42.1** to send command requests.
	
## JSON Requests List ##

| Command ID | Category           | Description                                                                                                                                | Example Json Request Body                  |
|------------|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------|
| 1001       | Capture Settings   | Set capture mode to visible                                                                                                                | { "commandId": 1001, "value": "" }         |
| 1002       | Capture Settings   | Set capture mode to thermal                                                                                                                | { "commandId": 1002, "value": "" }         |
| 1003       | Capture Settings   | Set capture mode to fused                                                                                                                  | { "commandId": 1003, "value": "" }         |
| 1101       | Inference Settings | Enable inference                                                                                                                           | { "commandId": 1101, "value": "" }         |
| 1102       | Inference Settings | Disable inference                                                                                                                          | { "commandId": 1102, "value": "" }         |
| 1103       | Inference Settings | Set inference mode to visible                                                                                                              | { "commandId": 1103, "value": "" }         |
| 1104       | Inference Settings | Set inference mode to thermal                                                                                                              | { "commandId": 1104, "value": "" }         |
| 1105       | Inference Settings | Set inference mode to fused                                                                                                                | { "commandId": 1105, "value": "" }         |
| 1106       | Inference Settings | Set inference engine to Yolo v2                                                                                                            | { "commandId": 1106, "value": "" }         |
| 1107       | Inference Settings | Set inference engine to Yolo v3                                                                                                            | { "commandId": 1107, "value": "" }         |
| 1108       | Inference Settings | Enable object tracking                                                                                                                     | { "commandId": 1108, "value": "" }         |
| 1109       | Inference Settings | Disable object tracking                                                                                                                    | { "commandId": 1109, "value": "" }         |
| 1110       | Inference Settings | Enable path tracking                                                                                                                       | { "commandId": 1110, "value": "" }         |
| 1111       | Inference Settings | Disable path tracking                                                                                                                      | { "commandId": 1111, "value": "" }         |
| 1201       | Fusion settings    | Set fusion value. The value can be 0-9 (inclusive) **Note: ‘value’ is mandatory**                                                              | { "commandId": 1201, "value": "0" }        |
| 1301       | Thermal settings   | Enable NUC                                                                                                                                 | { "commandId": 1301, "value": "" }         |
| 1302       | Thermal settings   | Disable NUC                                                                                                                                | { "commandId": 1302, "value": "" }         |
| 1303       | Thermal settings   | Change thermal palette. The value can be one of [blackhot, whitehot, fire, ice, dawn, dusk, davlut, kryptonite] **Note: ‘value’ is mandatory** | { "commandId": 1303, "value": "blackhot" } |
| 1304       | Thermal settings   | Enable edge detection                                                                                                                      | { "commandId": 1304, "value": "" }         |
| 1305       | Thermal settings   | Disable edge detection                                                                                                                     | { "commandId": 1305, "value": "" }         |
| 1401       | Media controls     | Start video recording on the server                                                                                                        | { "commandId": 1401, "value": "" }         |
| 1402       | Media controls     | Stop video recording on the server                                                                                                         | { "commandId": 1402, "value": "" }         |
| 1403       | Media controls     | Start raw frame dump on the server                                                                                                         | { "commandId": 1403, "value": "" }         |
| 1404       | Media controls     | Stop raw frame dump on the server                                                                                                          | { "commandId": 1404, "value": "" }         |
| 1601       | Capture settings   | Set brightness. The value can be 0-9 (inclusive) **Note: ‘value’ is mandatory**                                                                | { "commandId": 1601, "value": "5" }        |
| 1602       | Capture settings   | Set contrast. The value can be 0-9 (inclusive) **Note: ‘value’ is mandatory**                                                                  | { "commandId": 1602, "value": "5" }        |
| 1603       | EO settings        | Enable ICR mode                                                                                                                            | { "commandId": 1603, "value": "" }         |
| 1604       | EO settings        | Disable ICR mode                                                                                                                           | { "commandId": 1604, "value": "" }         |
| 1605       | EO settings        | Set zoom level. The value can be 0-9 (inclusive). The zoom level to value mapping is 1x zoom = 0, 2x zoom = 1, 3x zoom = 2, 5x zoom = 3, 8x zoom = 4, 10x zoom = 5, 15x zoom = 6, 20x zoom = 7, 25x zoom = 8, 30x zoom = 9. **Note: ‘value’ is mandatory** | { "commandId": 1605, "value": "0" } |

## RTSP video from Jade Systems ##

The RTSP URL of the live video stream from Jade system is **rtsp://192.168.42.1:8554/test**

## Steps to get synced inference metadata ##
Inference metadata is exposed as `JSON object` on port no **4042**. Each JSON object contains a related **frame ID**. The same **frame ID** is overlayed on top of each frame. Using the **frame ID**, the inference metadata can be synced with the corresponding frame.

To get the inference metadata, the client application needs to create a `websocket-client` and listen on port no **4042** at IP address **192.168.42.1**

[This is an example code](./data_websocket.py) to get inference metadata
	


Example Inference metadata format:

```javascript
{ 
  "Type": "Inference", 
  "Frame ID": 25, 
  "bboxes":  [
    {"x": 0.000000, 
    "y": 113.902451, 
    "width": 438.738373, 
    "height": 345.207336, 
    "label": "Person" }
  ] 
}
```

## How to use provided Jade client ##
1. Download the **bin.zip** from releases tab. 
2. Extract the zip
3. Run the following commands to execute the binary on linux client
```bash
$ cd bin/
$ ./rtsp_app
``` 
