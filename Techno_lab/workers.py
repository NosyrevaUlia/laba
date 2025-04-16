from datetime import datetime

def get_timestamp():
    return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))

# словарь со значениями Персонажей
WORKERS = {
    "Петрович": {
        "fname": "Кобан",
        "lname": "Петрович",
        "timestamp": get_timestamp(),
    },
    "Просп": {
        "fname": "Нортон",
        "lname": "Ruprecht",
        "timestamp": get_timestamp(),
    },
    "Проклятая": {
        "fname": "Патрисия",
        "lname": "Не помню",
        "timestamp": get_timestamp(),
    }
}

def read_all():
    return list(WORKERS.values())
