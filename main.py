from utils.file import get_todays_log
from ffxiv.log import translate_log, record_kill, LOG_LINE, CHANGE_ZONE, record_result


def read_match_data():
    log_path = get_todays_log()
    if not log_path:
        return

    with open(log_path, "r", encoding="UTF-8") as file:
        for line in file:
            event, log = translate_log(line)

            match event:
                case "LogLine":
                    record_kill(log)
                    record_result(log)
                case "ChangeZone":
                    print(log)

        file.close()


read_match_data()
