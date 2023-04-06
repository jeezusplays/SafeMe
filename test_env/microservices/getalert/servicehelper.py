from invokes import invoke_http
from threading import Thread
from os import environ
from time import sleep

SERVICEHELPER_HOST_PORT = environ.get("SERVICEHELPER_HOST_PORT")
SERVICEHELPER_URL = f"http://servicehelper:{SERVICEHELPER_HOST_PORT}"
print(SERVICEHELPER_URL)

def isServiceReady(servicename):
    try:
        r = invoke_http(f"{SERVICEHELPER_URL}/services/ready/{servicename}","GET")
        code = r.get("code",500)
        print(f"Checking if service ({servicename}) is ready: {code in range(200,300)}")
        if code in range(200,300):
            print(r['message'])
            return bool(r['message'])
    except Exception as e:
        return False
    return False

def _serviceIsReady(servicename):
    sleep(1)
    r = invoke_http(f"{SERVICEHELPER_URL}/services/ready/set/{servicename}","GET")
    return r['code'] in range(200,300)

def serviceIsReady(servicename):
    _t = Thread(target=_serviceIsReady,args=(servicename,))
    _t.start()
    