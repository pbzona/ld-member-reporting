import time
from datetime import timedelta
from ld_member_activity.config import Config


# Construct a URL to use in API requests
def create_url(route: str) -> str:
    cfg = Config().instance
    return f"{cfg.base_url}{cfg.url_prefix}{route}"


# Get the current UNIX timestamp (milliseconds)
def get_timestamp_for_now() -> int:
    return int(time.time()) * 1000


# Get the UNIX timestamp (ms) for today, minus some number of days
def get_timestamp_for_n_days_ago(num_days: int) -> int:
    now = get_timestamp_for_now()
    n_days_ago = now - num_days * 24 * 60 * 60 * 1000
    return n_days_ago


# Return the number of days that have elapsed since the given UNIX timestamp
def get_time_diff_in_days(timestamp=0) -> str | int:
    if timestamp == 0:
        return 'never'
    now = get_timestamp_for_now()
    difference = now - timestamp
    delta = timedelta(milliseconds=difference)
    return delta.days


# Return a base object to be used as query params for a request
def create_payload(filter_param: str) -> dict[str, str]:
    cfg = Config().instance
    return {
        "limit": str(cfg.member_limit),
        "filter": filter_param
    }
