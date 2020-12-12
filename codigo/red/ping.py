import os
import sys

ip = '192.168.1.1'

def ping(ip):
    
    response = os.system('ping ' + ip + ' -t')
    return response


data = ping(ip=ip)
print(data)