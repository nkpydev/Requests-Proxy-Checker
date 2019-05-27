from Utils.utils_configs import DATA_DIR
from Core.proxy_checker import ProxyChecker

ip = ['2.2.2.2','181.214.79.3']
port = '3129'

result = []

for i in ip:
    check = ProxyChecker()
    result.append(check.ip_resolver(i,port,'http://google.com'))
print(result)