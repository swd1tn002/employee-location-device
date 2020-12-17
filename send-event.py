# built on top of https://github.com/Azure/azure-iot-sdk-python/tree/master/azure-iot-device/samples

import os
import asyncio
import json
from azure.iot.device.aio import IoTHubDeviceClient
from random import random
from dotenv import load_dotenv

load_dotenv()

conn_str = os.getenv("IOTHUB_DEVICE_CONNECTION_STRING")

if not conn_str:
    print(f'Environment variable IOTHUB_DEVICE_CONNECTION_STRING is not set.')
    exit()


async def main():

    device_client = IoTHubDeviceClient.create_from_connection_string(conn_str)

    await device_client.connect()

    lat, lon = get_location()

    message = json.dumps({
        "lat": lat,
        "lon": lon,
    })

    print(f'Sending message {message}')

    await device_client.send_message(message)

    print('Message sent!')

    await device_client.disconnect()


def get_location():
    """
    Returns a random point inside Haaga-Helia Pasila campus area
    """
    lat = random_between(60.201982, 60.201286)
    lon = random_between(24.933579, 24.934879)

    return lat, lon


def random_between(a, b):
    diff = max(a, b) - min(a, b)
    return min(a, b) + random() * diff


if __name__ == "__main__":
    asyncio.run(main())
