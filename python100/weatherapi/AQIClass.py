from typing import Any
from dataclasses import dataclass
import json
@dataclass
class Category:
    Number: int
    Name: str

    @staticmethod
    def from_dict(obj: Any) -> 'Category':
        _Number = int(obj.get("Number"))
        _Name = str(obj.get("Name"))
        return Category(_Number, _Name)

@dataclass
class Root:
    DateObserved: str
    HourObserved: int
    LocalTimeZone: str
    ReportingArea: str
    StateCode: str
    Latitude: float
    Longitude: float
    ParameterName: str
    AQI: int
    Category: Category

    @staticmethod
    def from_dict(obj: Any) -> 'Root':
        _DateObserved = str(obj.get("DateObserved"))
        _HourObserved = int(obj.get("HourObserved"))
        _LocalTimeZone = str(obj.get("LocalTimeZone"))
        _ReportingArea = str(obj.get("ReportingArea"))
        _StateCode = str(obj.get("StateCode"))
        _Latitude = float(obj.get("Latitude"))
        _Longitude = float(obj.get("Longitude"))
        _ParameterName = str(obj.get("ParameterName"))
        _AQI = int(obj.get("AQI"))
        _Category = Category.from_dict(obj.get("Category"))
        return Root(_DateObserved, _HourObserved, _LocalTimeZone, _ReportingArea, _StateCode, _Latitude, _Longitude, _ParameterName, _AQI, _Category)

# Example Usage
# jsonstring = json.loads(myjsonstring)
# root = Root.from_dict(jsonstring)
