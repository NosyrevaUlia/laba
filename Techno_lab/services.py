from datetime import datetime

def get_timestamp():
    return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))

# словарь со значениями Персонажей
SERVICES = {
    "Помыв": {
        "Вид автомобиля": "грузовой",
        "timestamp": get_timestamp(),
    },
    "Помыв": {
        "Вид автомобиля": "легковой",
        "timestamp": get_timestamp(),
    }
}

def read_all():
    return list(SERVICES.values())