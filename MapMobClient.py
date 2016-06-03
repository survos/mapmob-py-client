import json
try:
    from urllib.parse import urlparse, urlencode
    from urllib.request import urlopen, Request
    from urllib.error import HTTPError
except ImportError:
    from urlparse import urlparse
    from urllib import urlencode
    from urllib2 import urlopen, Request, HTTPError


DEFAULT_BASE_URL = "http://mapmob.com/api"

class MapMobClient(object):
    def __init__(self, base_url=DEFAULT_BASE_URL):
        self.__base_url = base_url

    def authorize(self, login, password):
        url = self.__base_url + "/security/login"
        data = urlencode({"username": login, "password": password})
        req = Request(url, data=data.encode("utf-8"))
        try:
            connection = urlopen(req)
        except (HTTPError) as e:
            connection = e
            self.__latest_error = connection.read().decode("utf-8")

        if connection.code == 200:
            html = connection.read().decode("utf-8")
            json_obj = json.loads(html)
            self.__token_string = json_obj["accessToken"]
            return True
        else:
            return False

    def register(self, email, login, password):
        url = self.__base_url + "/security/register"
        data = urlencode({"email": email, "username": login, "plainPassword": password})
        req = Request(url, data=data.encode("utf-8"))
        try:
            connection = urlopen(req)
        except (HTTPError) as e:
            connection = e
            self.__latest_error = connection.read().decode("utf-8")

        return connection.code == 201
    def get_latest_error(self):
        return self.__latest_error

