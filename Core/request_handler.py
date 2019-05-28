# ---- Requests Imports ---- #
import requests
from requests.exceptions import ProxyError,HTTPError,TooManyRedirects,Timeout,SSLError,ConnectTimeout


class ProxyChecker():
    def __init__(self):
        self.target_url = ''
        self.proxies = ''
        self.user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'
        self.headers = ''
        self.time_out = 30
        #self.return_list = []
        #self.return_list.clear()

    def ip_resolver(self,ip,port,target_url):
        self.headers = {'User-Agent': self.user_agent}
        self.proxies = {'http': 'http://{}:{}'.format(ip,port)}

        try:
            pro = requests.get(target_url,timeout=self.time_out,proxies=self.proxies,headers=self.headers)
            return [ip,target_url,pro.status_code]
        except Exception as ex:
            return [ip,target_url,ex]