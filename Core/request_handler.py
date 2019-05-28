# ---- Requests Imports ---- #
import requests
# --- Project Internal Imports --- #
# --- Exceptions --- #
from requests.exceptions import ProxyError,HTTPError,TooManyRedirects,Timeout,SSLError,ConnectTimeout

# --- Class ProxyChecker, which will have a 'ip_resolver()' function to do requests and get status_code or exception --- #
class ProxyChecker():
    def __init__(self):
        self.target_url = ''
        self.proxies = ''
        self.user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'
        self.headers = ''
        self.time_out = 30
        #self.return_list = []
        #self.return_list.clear()

    # --- Function to do requests and accordingly either get status_code[mostly SUCCESS] or exception [NOT WORKING]
    def ip_resolver(self,ip,port,target_url):
        self.headers = {'User-Agent': self.user_agent}
        self.proxies = {'http': 'http://{}:{}'.format(ip,port)}
        # For Authenticated Proxies, use below line:
        # {'http':'http://{}:{}@{}.{}'.format(auth_user,auth_pwd,ip,port)}
        # Kindly note: store your auth_user and auth_pwd as variables, before your use this line.

        try:
            pro = requests.get(target_url,timeout=self.time_out,proxies=self.proxies,headers=self.headers)
            return [ip,target_url,pro.status_code]
        except Exception as ex:
            return [ip,target_url,ex]