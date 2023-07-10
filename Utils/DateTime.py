from datetime import datetime


class DateTime:
    def get_time(self) -> datetime:
        return datetime.now()

    # Return current local date in ISO 8601 format
    def get_time_formatted(self) -> str:
        return datetime.now().strftime("%Y-%m-%dT%H:%M:%S")
