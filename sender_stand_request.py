import requests
import configuration
import data


def create_courier():
    response = requests.post(
        configuration.URL_SERVICE + configuration.CREATE_COURIER,
        headers=data.headers,
        json=data.courier_body
    )
    return response


def create_order():
    response = requests.post(
        configuration.URL_SERVICE + configuration.CREATE_ORDER,
        headers=data.headers,
        json=data.order_body
    )
    return response


def get_order_by_track(track):
    url = f"{configuration.URL_SERVICE}{configuration.GET_ORDER_TRACK}?t={track}"
    response = requests.get(url, headers=data.headers)
    return response
