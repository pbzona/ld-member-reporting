import requests
from requests import Response

from ld_member_activity.config import Config
from ld_member_activity.utils import create_url, create_payload, get_timestamp_for_n_days_ago

class LaunchDarklyApi:
    def __init__(self):
        self.config = Config().instance

    def get_members(self, payload=None) -> Response:
        if payload is None:
            payload = {"limit": self.config.member_limit}
        r = requests.get(url=create_url("/members"), headers=self.config.headers, params=payload)
        return r

    def delete_member(self, member_id) -> Response:
        r = requests.post(url=create_url(f"/members/{member_id}"), headers=self.config.headers)
        return r
