
import time
import socket

import psutil
import requests


def get_hostname():
    return { 'hostname' : socket.gethostname() }

def get_mem_info():
    meminfo = {}
    mem = psutil.virtual_memory()
    #print mem.total
    #print mem.available
    #print mem.used
    mem_free = int(mem.free) + int(mem.buffers) + int(mem.cached)
    meminfo['mem_free'] = mem_free / 1024 /1024
    return meminfo

def send(data):
    req = requests.post(url='http://127.0.0.1:8000/api/v1/monitor', data=data)
    print req.status_code
    print req.text

def autocollect():
    data = {}
    data.update(get_mem_info())
    data.update(get_hostname())
    data.update({'create_time' : int(time.time()) })

    send(data)

def main():

    while True:
        autocollect()
        time.sleep(5)
 



if __name__ == '__main__':
    main()
