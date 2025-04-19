import re

LOG_LINE = "LogLine"
CHANGE_ZONE = "ChangeZone"

CHANGE_ZONE_REGEX = (
    r"^(?P<type>01)\|(?P<timestamp>[^|]*)\|(?P<id>[^|]*)\|(?P<name>[^|]*)\|"
)
LOG_LINE_REGEX = r"^(?P<type>00)\|(?P<timestamp>[^|]*)\|(?P<code>[^|]*)\|(?P<name>[^|]*)\|(?P<line>[^|]*)\|"


def translate_log(line: str) -> tuple[str, str]:
    parsed_line = line.split("|")

    match parsed_line[0]:
        case "00":
            match = re.search(LOG_LINE_REGEX, line)
            if match:
                return LOG_LINE, match.group("line")
        case "01":
            match = re.search(CHANGE_ZONE_REGEX, line)
            if match:
                return CHANGE_ZONE, match.group("name")

    return "", ""


YOUR_KILL_REGEX = r"You defeat (?P<enemy>.*)."
YOUR_DEATH_REGEX = r"You are defeated by (?P<enemy>.*)."
TEAM_KILL_REGEX = r"(?P<teammate>.*) defeats (?P<enemy>.*)."
ENEMY_KILL_REGEX = r"(?P<teammate>.*) are defeated by (?P<enemy>.*)."

kill_regex_list = [
    YOUR_KILL_REGEX,
    YOUR_DEATH_REGEX,
    TEAM_KILL_REGEX,
    ENEMY_KILL_REGEX,
]


def record_kill(log_line: str):
    if "defeat" in log_line:
        for regex in kill_regex_list:
            match = re.search(regex, log_line)

            if match:
                print(log_line)


WOLF_MARK_REGEX = r"You obtain (?P<amount>\d+) Wolf Marks."


def record_result(log_line: str):
    if "Wolf Marks" in log_line:
        match = re.search(WOLF_MARK_REGEX, log_line)

        if match:
            amount = match.group("amount")

            if amount == "500":
                print("YOU WON")
            else:
                print("YOU LOST")
