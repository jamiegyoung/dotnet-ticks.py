from datetime import datetime, timedelta


def ticks_from_datetime(dt: datetime):
    """Convert datetime to .Net ticks"""
    if type(dt) is not datetime:
        raise TypeError('dt must be a datetime object')
    return (dt - datetime(1, 1, 1)).total_seconds() * 10000000
    # print("{:f}".format(datetime(1, 1, 1).timestamp()))
    # return (dt.timestamp() * 10000000)


def datetime_from_ticks(ticks: float):
    """Convert .Net ticks to datetime"""
    if type(ticks) is not float:
        raise TypeError('ticks must of type float or int')
    return datetime(1, 1, 1) + timedelta(microseconds=ticks / 10)
