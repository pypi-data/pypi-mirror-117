<h1 align=center>enum-prop</h1>

<p align=center>
    <a href=https://github.com/5m/enum-prop/actions?query=workflow%3ACI+branch%3Amain><img src=https://github.com/5m/enum-prop/workflows/CI/badge.svg alt="CI Build Status"></a>
</p>

Enum definitions can't, for good reasons, reference instances of themselves within their
own definitions. This module allows definitions to come around that by mapping the names
of enums for lookups, hidden behind a special dict subclass. This allows enum
definitions to remain tidy, and avoids having to define instance-specific configuration
as property functions.

### Installation

```shell
$ python3 -m pip install enum-prop
```

### Usage

```python
import enum
from enum_prop import enum_property, enum_getter

class Vehicle(enum.Enum):
    car = "car"
    bike = "bike"
    unicycle = "unicycle"
    wheels = enum_property({car: 4, bike: 2, unicycle: 1})
    __int__ = enum_getter({car: 4, bike: 2, unicycle: 1})

print(Vehicle.unicycle.wheels)  # 1
print(Vehicle.car.wheels)  # 4
print(int(Vehicle.unicycle))  # 1
print(int(Vehicle.bike))  # 2
```
