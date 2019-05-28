from Utils.utils_configs import INPUT_FILE,OUTPUT_FILE
from Core.request_handler import ProxyChecker
from Core.exceptions import ProxyCheckerDirHandlingError, ProxyCheckerRequestException
#import csv

port = '2007' # Change Port to your need

target_urls = ['http://google.com',
                'http://github.com',
                'http://msn.com'                
            ]

result = []

with open(INPUT_FILE,'r') as rf:
    in_put = rf.readlines()
    for ip in in_put:
        for url in target_urls:
            check = ProxyChecker()
            result.append(check.ip_resolver(ip,port,url))

print(result)
# ---------------------------------------------------------- #
""" This the part for which I am stuck, working on it!! """
# with open(OUTPUT_FILE,'w') as of:
#     for entry in result:
#         of.write(entry)
# ---------------------------------------------------------- #
