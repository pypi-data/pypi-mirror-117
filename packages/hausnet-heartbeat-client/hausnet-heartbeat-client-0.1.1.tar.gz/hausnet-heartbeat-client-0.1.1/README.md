A thin wrapper for the HausNet Heartbeat service, in Python. Heartbeat is a monitoring 
service for home automation networks, e.g. a home controlled by [Home Assistant](https://homeassistant.com).  

If you are running Home Assistant, follow the instructions for setting up the 
[Hausnet Heartbeat](https://app.hausnet.io/heartbeat/docs) component. 
The package for this module is included as a dependency of the component. 

Installation
============

On Home Assistant, this package will be automatically installed as a dependency of the Hausnet Heartbeat
component.

For use elsewhere, install the package on your client:
```
pip install hausnet_heartbeat_client
```

Configuration
=============

On Home Assistant, follow the instructions for setting up the Hausnet Heartbeat component.

Elsewhere, sign up at [HausNet](https://app.hausnet.io), and copy the app authentication token
from your profile page on the app site. Then, define a device on the app site to represent your 
home automation system. You'll need the device name and authentication token from the service to
connect this client.

Use
===

The library provides access to a device's heartbeat monitor. I.e. it enables your home 
control system to, at a 15-minute interval, let the monitor know it is still alive. 

The system should send a heartbeat (i.e. call the send_heartbeat function) every 15 minutes. If the service
does not receive the next heartbeat signal in that time frame, it will alert you via email that your
home automation system is not responding. It will also let you know when it starts responding again.

The heartbeat monitor should not be called more often than every 15 minutes, as that will result
in service suspension.

```
from heartbeat_client.client import HeartbeatClient

API_URL = "https://app.hausnet.io/heartbeat/api"
API_TOKEN = "[token from HausNet user account]"
DEVICE_NAME = "[device name at HausNet]"

client = HeartbeatClient(API_URL, API_TOKEN)
heartbeat = self._client.get_heartbeat(DEVICE_NAME)
client.send_heartbeat(heartbeat['id'])
```

