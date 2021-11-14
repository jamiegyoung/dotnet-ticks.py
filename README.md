# dotnet-ticks.py
converts python datetime to and from .Net ticks

This is a work in progress.

The accuracy of this conversion is not guaranteed and has not been thoroughly tested.
See the issue example below for more information.

## Usage
```py
from dotnet_ticks import ticks_from_datetime, datetime_from_ticks
from datetime import datetime

current_time = datetime.now()

print(datetime_from_ticks(ticks_from_datetime(current_time)).timestamp())

```

## Issues
```py
print(current_time.timestamp())
print(datetime_from_ticks(ticks_from_datetime(current_time)).timestamp())
```
returns two very similar times, but different by a few milliseconds.
```
1636907926.042607
1636907926.042608
```