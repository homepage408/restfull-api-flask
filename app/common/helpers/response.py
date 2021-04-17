from flask import jsonify


def success(values, message):
    res = {
        "data": values,
        "message": message
    }

    return res


def badRequest(values, message):
    res = {
        "data": values,
        "message": message
    }
    return res


def tokenSuccess(data, values, message="Success"):
    res = {
        "data": data,
        "payload": values,
        "message": message
    }
    return res
