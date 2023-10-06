from ld_member_activity.utils import get_time_diff_in_days

field_names = [
    "id",
    "firstName",
    "lastName",
    "email",
    "lastSeen",
    "verified",
    "pendingInvite"
]


class Member:
    @staticmethod
    def get_fields():
        return field_names

    def __init__(self, member):
        if not member:
            raise Exception("Must provide a member object")

        self.id = member["_id"]

        try:
            self.firstName = member["firstName"]
        except KeyError:
            self.firstName = "NONE"

        try:
            self.lastName = member["lastName"]
        except KeyError:
            self.lastName = "NONE"

        try:
            self.email = member["email"]
        except KeyError:
            self.email = "NONE"

        try:
            self.lastSeen = member["_lastSeen"]
        except KeyError:
            self.lastSeen = None

        try:
            self.verified = member["_verified"]
        except KeyError:
            self.verified = None

        try:
            self.pending = member["_pendingInvite"]
        except KeyError:
            self.pending = None

    @property
    def days_since_last_seen(self):
        value = "never"
        if self.lastSeen is None:
            return value

        try:
            days_since_last_seen = get_time_diff_in_days(self.lastSeen)
            if days_since_last_seen == 0:
                return value
            value = f"{days_since_last_seen} days ago"
        except Exception as e:
            raise e

        return value

    def to_dict(self):
        res = {}
        for field in field_names:
            if field == "lastSeen":
                res[field] = self.days_since_last_seen
            else:
                res[field] = self[field]
        return res

    def __getitem__(self, item):
        match item:
            case "id":
                return self.id
            case "firstName":
                return self.firstName
            case "lastName":
                return self.lastName
            case "email":
                return self.email
            case "lastSeen":
                return self.lastSeen
            case "verified":
                return self.verified
            case "pending":
                return self.pending
            case _:
                return None
