import os
from datetime import date

LOG_PATH = os.path.join(os.getenv("APPDATA"), "Advanced Combat Tracker", "FFXIVLogs")  # type: ignore


def get_todays_log() -> str | None:
    today = date.today()
    today_str = today.strftime("%y%m%d")

    files = os.listdir(LOG_PATH)
    for file in files:
        if today_str in file:
            return os.path.join(LOG_PATH, file)
    return None


print(get_todays_log())
