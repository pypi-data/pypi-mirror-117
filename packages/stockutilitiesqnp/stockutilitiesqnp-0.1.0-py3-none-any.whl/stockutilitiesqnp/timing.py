from math import floor
import time as t
from datetime import datetime, date, time
from dateutil import tz, parser
from typing import List


DAY_IN_MILLISECONDS = 86400000


def epoch_second() -> int:
    return floor(t.time())


def epoch_millisecond() -> int:
    return floor(t.time() * 1000)


def datetime_ny(timestamp=None) -> datetime:
    if timestamp is None:
        return datetime.now(tz.gettz('America/New_York'))
    else:
        return datetime.fromtimestamp((timestamp / 1000), tz.gettz('America/New_York'))


def datetime_ny_str(timestamp=None) -> str:
    return datetime_ny(timestamp).strftime("%Y-%m-%d %H:%M:%S")


def date_ny(timestamp=None) -> date:
    if timestamp is None:
        return datetime.now(tz.gettz('America/New_York')).date()
    else:
        return datetime.fromtimestamp((timestamp / 1000), tz.gettz('America/New_York')).date()


def date_ny_str(timestamp=None) -> str:
    return datetime_ny(timestamp).strftime("%Y-%m-%d")


def time_ny(timestamp=None) -> time:
    if timestamp is None:
        return datetime.now(tz.gettz('America/New_York')).time()
    else:
        return datetime.fromtimestamp((timestamp / 1000), tz.gettz('America/New_York')).time()


def time_ny_str(timestamp=None) -> str:
    return datetime_ny(timestamp).strftime("%H:%M:%S")


def str_to_datetime_ny(date_: str, time_: str) -> datetime:
    tzinfos = {"CST": tz.gettz("America/New_York")}
    return parser.parse(f'{date_} {time_} CST', tzinfos=tzinfos)


def str_to_timestamp_ny(date_: str, time_: str) -> int:
    tzinfos = {"NY": tz.gettz("America/New_York")}
    return floor(parser.parse(f'{date_} {time_} NY', tzinfos=tzinfos).timestamp() * 1000)


def ny_timestamp(year: int, month: int = 1, day: int = 1, hour: int = 0, minute: int = 0, second: int = 0, millisecond: int = 0) -> int:
    return floor(datetime(year, month, day, hour, minute, second, millisecond * 1000,
                          tzinfo=tz.gettz("America/New_York")).timestamp() * 1000)


def date_range(start_date: str, end_date: str) -> List[str]:
    result = []
    current_timestamp = str_to_timestamp_ny(start_date, "00:00")
    while start_date <= end_date:
        result.append(start_date)
        current_timestamp += DAY_IN_MILLISECONDS
        start_date = date_ny_str(current_timestamp)
    return result

