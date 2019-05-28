# --- Generic Imports --- #
import csv

# --- Project Internal Imports --- #
from Utils.utils_configs import INPUT_FILE,OUTPUT_FILE
from Core.request_handler import ProxyChecker
from Core.exceptions import ProxyCheckerDirHandlingError, ProxyCheckerRequestException


# --- Port Number --- #
port = '2007' # Change Port to your need

# --- Target URLs --- #
# Change URLs as per your choice
target_urls = ['http://google.com',
                'http://github.com',
                'http://msn.com'                
            ]

# --- End Result Store into List --- #
result = []

# --- Open input.txt and read lines, process 1 at a time, store return into a list --- #
with open(INPUT_FILE,'r') as rf:
    in_put = rf.readlines()
    for ip in in_put:
        if "\n" in ip:
            ip = ip.split('\n')
            new_ip = ip[0]
        else:
            new_ip = ip    
        for url in target_urls:
            check = ProxyChecker()
            result.append(check.ip_resolver(new_ip,port,url))
# --- Open output.csv and writerow, 1 at a time from the result [list] --- #
with open(OUTPUT_FILE,'w',newline='') as of:
    writer = csv.writer(of)
    writer.writerows(result)
print('DONE!!')