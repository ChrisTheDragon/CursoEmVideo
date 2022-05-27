import requests

def check_internet():
    url = 'http://pudim.com.br/'
    timeout = 5
    try:
        requests.get(url, timeout=timeout)
        return True
    except ConnectionError:
        return False


if check_internet():
    print(f'Pudim está online')
else:
    print(f'Pudim está offline')