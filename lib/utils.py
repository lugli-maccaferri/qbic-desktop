import requests
import json
import os


def get_post_request(get, address, route, data=None, headers=None, delete=False):
    if data is None:
        data = {}
    if headers is None:
        headers = {}

    if not isinstance(get, bool):
        raise Exception("Wrong format for \"get\" parameter (must be bool)")

    address = address.rstrip("/")

    if not route.startswith("/"):
        route = "/" + route

    try:
        if delete:
            r = requests.delete(address + route, headers=headers, json=data)
        elif get:
            r = requests.get(address + route, headers=headers, json=data)
        else:
            r = requests.post(address + route, headers=headers, json=data)
    except requests.exceptions.ConnectionError:
        raise Exception("Connection to \"" + address + route + "\" failed")
    except requests.exceptions.HTTPError:
        raise Exception("Connection request returned an invalid HTTP response")
    except requests.exceptions.Timeout:
        raise Exception("Connection request timed out")
    except requests.exceptions.TooManyRedirects:
        raise Exception("Too many redirects during connection request")
    except requests.exceptions.RequestException:
        raise Exception("Unknown error during connection request")

    flag = True

    if r.status_code == 401:
        raise Exception("Unauthorized (401)")
    elif r.status_code == 400:
        raise Exception("Bad request (400)")
    elif 200 <= r.status_code < 300:
        flag = False
    else:
        raise Exception("Unexpected error (HTTP status code " + str(r.status_code) + ")")

    try:
        rjson = r.json()
    except json.decoder.JSONDecodeError:
        raise Exception("The specified server did not return a valid json response")

    if "success" not in rjson:
        raise Exception("The specified server returned an unexpected json response")

    if flag:
        raise Exception("Unknown error")

    return rjson


def tokenized_get_post_request(get, address, route, data, token, delete=False):
    if token is None:
        raise Exception("token is None")

    headers = {
        "Authorization": "Bearer " + token
    }

    try:
        return get_post_request(get, address, route, data, headers, delete)
    except Exception as e:
        if "(401)" in str(e):
            raise Exception("Wrong token")
        raise Exception(str(e))


def load_underlying_mc_servers_number(label, host, button):
    route = "/server/list"

    try:
        servers = get_post_request(True, host, route)["servers"]
        button.setEnabled(True)
        label.setText(str(len(servers)))
    except Exception as e:
        print("Error while loading the count of MC servers for qbic server \"" + host + "\"")
        print("\t" + str(e))


def login_connect(address, username, password):
    route = "/auth/login"
    data = {'username': username, 'password': password}

    try:
        rjson = get_post_request(False, address, route, data)
    except Exception as e:
        if "(401)" in str(e):
            raise Exception("Wrong username or password")
        raise Exception(str(e))

    return rjson["token"]


def add_to_recent(address, username, recent_filename):

    found = False

    if os.path.exists(recent_filename):

        with open(recent_filename) as f:
            if address + " " + username in f.read():
                found = True

        append_write = 'a'  # append if already exists

    else:
        append_write = 'w'  # make a new file if not

    if not found:
        f = open(recent_filename, append_write)
        f.write(address + " " + username + '\n')
        f.close()

        f = open(recent_filename, "r")
        lines = f.readlines()
        if len(lines) > 5:
            f.close()
            f = open(recent_filename, "w")
            f.writelines(lines[len(lines) - 5:])
        f.close()
