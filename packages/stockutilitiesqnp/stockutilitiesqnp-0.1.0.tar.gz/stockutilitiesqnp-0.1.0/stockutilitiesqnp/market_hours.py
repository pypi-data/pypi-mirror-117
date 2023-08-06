import json
import importlib.resources
from . import timing

market_hours = {}


def _load_data():
    with importlib.resources.path(__package__, 'market-hours-data.json') as data_path:
        with open(data_path) as data_file:
            data = json.load(data_file)
            for item in data:
                market_hours[item['date']] = item


_load_data()


def is_market_open(time: int = None) -> bool:
    if time is None:
        time = timing.epoch_millisecond()
    operating_hour = market_hours.get(timing.date_ny_str(time))
    if operating_hour is None:
        return False
    else:
        return timing.str_to_timestamp_ny(operating_hour['date'], operating_hour['open']) <= time \
               <= timing.str_to_timestamp_ny(operating_hour['date'], operating_hour['close'])


def get_market_hours(time=None):
    if isinstance(time, str):
        return market_hours.get(time)
    elif isinstance(time, int):
        return market_hours.get(timing.date_ny_str(time))
    else:
        return market_hours.get(timing.date_ny_str())


def is_trading_day(time=None) -> bool:
    return get_market_hours(time) is not None
