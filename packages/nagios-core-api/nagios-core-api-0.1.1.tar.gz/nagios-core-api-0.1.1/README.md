# nagios-core-api
A python wrapper for querying nagios core monitoring

## Note:
This module is *work-in-progress*.

## Usage:


```python
from nagios import Nagios

with Nagios(
    url="https://nagios.monitor.com/nagios",
    username="nagiosuser",
    password="nagiospassword",
) as client:
    response = client.status.service_list(hostname="machine1")
    print(response)
```
