# Aio Moneta client

This client for moneta merchant api https://www.moneta.ru/doc/MONETA.MerchantAPI.v2.ru.pdf


## Instalation

```shell
pip install aiomonetaclient
```


## Usage

```python
import asyncio
from aiomonetacleint import Client


if __name__ == '__main__':
    moneta_client = Client(
        username='<moneta username>',
        password='<moneta password>'
    )
    loop = asyncio.get_event_loop()
    profiles = loop.run_until_complete(
        # request FindProfileRequest
        moneta_client.find_profile_info(
            '<phone without +>'
        )
    )
    # print first profile attributes
    print(profiles.Envelope.Body.FindProfileInfoResponse.to_json(indent=4))
```