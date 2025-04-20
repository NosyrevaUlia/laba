from datetime import datetime
from flask import abort, make_response

def get_timestamp():
    return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))

WORKERS = {
    "Wilding": {
        "fname": "Petrovich",
        "lname": "Petro",
        "timestamp": get_timestamp(),
    },
    "Prospector": {
        "fname": "Norton",
        "lname": "Ruprecht",
        "timestamp": get_timestamp(),
    },
    "Enchantress": {
        "fname": "Patricia",
        "lname": "Dorvald",
        "timestamp": get_timestamp(),
    }
}

def read_all():
    return list(WORKERS.values())

def create(worker):
    lname = worker.get("lname")
    fname = worker.get("fname", "")

    if lname and lname not in WORKERS:
        WORKERS[lname] = {
            "lname": lname,
            "fname": fname,
            "timestamp": get_timestamp(),
        }
        return WORKERS[lname], 201
    else:
        abort(
            406,
            f"Worker with last name {lname} already exists",
        )

def read_one(lname):
    if lname in WORKERS:
        return WORKERS[lname]
    else:
        abort(
            404, f"Worker with last name {lname} not found"
        )

def update(lname, worker):
    if lname in WORKERS:
        WORKERS[lname]["fname"] = worker.get("fname", WORKERS[lname]["fname"])
        WORKERS[lname]["timestamp"] = get_timestamp()
        return WORKERS[lname]
    else:
        abort(
            404, f"Worker with last name {lname} not found"
        )

def delete(lname):
    if lname in WORKERS:
        del WORKERS[lname]
        return make_response(
            f"{lname} successfully deleted", 200
        )
    else:
        abort(
            404, f"Worker with last name {lname} not found"
        )