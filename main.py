from dotenv import load_dotenv

from ld_member_activity.config import Config
from ld_member_activity.member_list import MemberList
from ld_member_activity.utils import get_timestamp_for_n_days_ago


def main():
    cfg = Config().instance

    # Report for members who have not logged activity in 90+ days
    report_file = "reports/not_seen_in_90_days.csv"
    param_filter = f'lastSeen:{{"before":{get_timestamp_for_n_days_ago(cfg.time_limit)}}}'
    infrequent_members = MemberList(param_filter=param_filter, report_file=report_file)
    infrequent_members.log()

    # Report for users who have never logged in
    report_file = "reports/never_seen.csv"
    param_filter = 'lastSeen:{"never":true}'
    never_seen_members = MemberList(param_filter=param_filter, report_file=report_file)
    never_seen_members.log()

    # Report for users who were created before activity data was collected
    report_file = "reports/very_old.csv"
    param_filter = 'lastSeen:{"noData":true}'
    very_old_members = MemberList(param_filter=param_filter, report_file=report_file)
    very_old_members.log()


if __name__ == '__main__':
    load_dotenv()
    main()
