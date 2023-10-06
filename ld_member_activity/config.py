import os


# Decorator to enforce a singleton pattern on the Config object
def singleton(class_instance):
    instances = {}

    def get_instance(*args, **kwargs):
        if class_instance not in instances:
            instances[class_instance] = class_instance(*args, **kwargs)
        return instances[class_instance]

    return get_instance


@singleton
class Config:
    _instance = None

    def __init__(self):
        self._instance = self

        self.base_url = "https://app.launchdarkly.com"
        self.url_prefix = "/api/v2"
        self.api_token = os.environ.get("LD_API_TOKEN")
        self.headers = {"Authorization": self.api_token}

        self.dry_run = os.environ.get("DRY_RUN") != 0

        # Number of members to retrieve in each API request
        self.member_limit = 100

        # Reporting cutoff period in days
        self.time_limit = 90

    @property
    def instance(self):
        return self._instance
