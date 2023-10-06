import csv
from ld_member_activity.member import Member


class Report:
    def __init__(self, member_list):
        self.member_list = member_list
        self.file_name: str or None = None

    def set_file(self, file_name: str):
        self.file_name = file_name

    def write_to_csv_file(self):
        if self.file_name is None:
            raise TypeError("You must use set_file before attempting to write the report to disk")
        with open(self.file_name, "w", newline="") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=Member.get_fields())
            writer.writeheader()
            for member in self.member_list:
                m = member.to_dict()
                writer.writerow(m)

