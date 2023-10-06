from ld_member_activity.api import LaunchDarklyApi
from ld_member_activity.member import Member
from ld_member_activity.report import Report
from typing import List

from ld_member_activity.utils import create_payload


class MemberList:
    def __init__(self, param_filter: str, report_file: str, fetch_on_init: bool = True):
        self.payload = create_payload(param_filter)
        self.members: List[Member] = []

        self.report = Report(self)
        self.report.set_file(report_file)

        self.api = LaunchDarklyApi()

        if fetch_on_init:
            self.fetch_members()

    def fetch_members(self) -> None:
        response = self.api.get_members(payload=self.payload)
        data = response.json()["items"]
        self.add_members(data)

    def add_members(self, members: List[any]) -> None:
        for m in members:
            try:
                member = Member(m)
                self.members.append(member)
            except KeyError as k:
                m[k] = "NA"
                member = Member(m)
                print(member)
                self.members.append(member)
            # except Exception as e:
            #     print(f"Could not add member {m['_id']} ({m['email']})")
            #     print(m[e])
            #     print(e)
            #     continue

    def log(self):
        self.report.write_to_csv_file()

    def __iter__(self):
        self._index = 0  # Initialize the index to 0
        return self

    def __next__(self):
        if self._index < len(self.members):
            member = self.members[self._index]
            self._index += 1
            return member
        else:
            raise StopIteration  # Raise StopIteration when there are no more elements

