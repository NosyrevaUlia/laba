from datetime import datetime
from flask import abort, make_response

def get_timestamp():
    return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))

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

def create(user):
    lname = user.get("lname")
    fname = user.get("fname", "")

    if lname and lname not in USERS:
        USERS[lname] = {
            "lname": lname,
            "fname": fname,
            "timestamp": get_timestamp(),
        }
        return USERS[lname], 201
    else:
        abort(
            406,
            f"User with last name {lname} already exists",
        )

def read_one(lname):
    if lname in USERS:
        return USERS[lname]
    else:
        abort(
            404, f"User with last name {lname} not found"
        )

def update(lname, user):
    if lname in USERS:
        USERS[lname]["fname"] = user.get("fname", USERS[lname]["fname"])
        USERS[lname]["timestamp"] = get_timestamp()
        return USERS[lname]
    else:
        abort(
            404, f"User with last name {lname} not found"
        )

def delete(lname):
    if lname in USERS:
        del USERS[lname]
        return make_response(
            f"{lname} successfully deleted", 200
        )
    else:
        abort(
            404, f"User with last name {lname} not found"
        )