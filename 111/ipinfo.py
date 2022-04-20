import requests

IPINFO_URL = 'http://ipinfo.io/{ip}/json'


def get_ip_country(ip_address):
    """Receives ip address string, use IPINFO_URL to get geo data,
        parse the json response returning the country code of the IP"""
    request_url = IPINFO_URL.replace("{ip}", ip_address)
    data = requests.get(request_url).json()
    return data["country"]
