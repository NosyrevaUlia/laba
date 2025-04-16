from datetime import datetime

def get_timestamp():
    return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))

# словарь со значениями Персонажей
USERS = {
    "Gardener": {
        "fname": "Emma",
        "lname": "Woods",
        "timestamp": get_timestamp(),
    },
    "Doc": {
        "fname": "Emily",
        "lname": "Dyer",
        "timestamp": get_timestamp(),
    },
    "Lucky": {
        "fname": "No",
        "lname": "Name",
        "timestamp": get_timestamp(),
    }
}

def read_all():
    return list(USERS.values())