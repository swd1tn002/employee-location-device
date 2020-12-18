# Azure IoT device test

This project emulates and IoT device and sends location telemetry to Azure IoT hub. Random coordinates near Haaga-Helia Pasila campus are defined in `send-event.py` as follows:

```python
lat = random_between(60.201982, 60.201286)
lon = random_between(24.933579, 24.934879)
```

Change the coordinates and logic based on your preferences.

## Sample code

The code in [send-event.py](send-event.py) is based on Azure SDK's sample at https://github.com/Azure/azure-iot-sdk-python/tree/master/azure-iot-device/samples. As in the sample, you must define an environment variable `IOTHUB_DEVICE_CONNECTION_STRING` with your device connection string before executing the script.

## Usage

To start sending locations to your IoT hub endpoint first clone this repository:

```
$ git clone https://github.com/swd1tn002/employee-location-device.git
$ cd employee-location-device
```

Then, install the dependencies defined in [requirements.txt](requirements.txt) and run the script:

```
$ pip install -r requirements.txt
$ python send-event.py
```

In Unix based systems you can run the script on regular intervals with the `watch` command:

```
$ watch -n 60 python send-event.py
```

## Docker alternative

Alternatively, you can run the script inside a Docker container. This way you do not need to install dependencies locally and you can deploy the container to your hosting provider. The `IOTHUB_DEVICE_CONNECTION_STRING` environment variable needs to be given as an argument for `docker run`:

```
$ docker build -t employee-location-test .
$ docker run -it -e IOTHUB_DEVICE_CONNECTION_STRING="YOUR_CONNECTION_STRING_HERE" --rm employee-location-test
```
