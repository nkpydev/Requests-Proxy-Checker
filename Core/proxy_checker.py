# ---- Requests Imports ---- #
import requests
from requests.exceptions import ProxyError,HTTPError,TooManyRedirects,Timeout


class ProxyChecker():
    def __init__(self):
        self.target_url = ''
        self.proxies = ''
        self.user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'
        self.headers = ''
        self.time_out = 30
        self.return_list = []

    def ip_resolver(self,ip,port,target_url):
        self.headers = {'User-Agent': self.user_agent}
        self.proxies = {'http': 'http://{}:{}'.format(ip,port)}

        try:
            pro = requests.get(target_url,timeout=self.time_out,proxies=self.proxies,headers=self.headers)
            self.return_list.append([ip,port,target_url,pro.status_code])
        except ProxyError as pe:
            self.return_list.append([ip,port,target_url,pe])
        except HTTPError as he:
            self.return_list.append([ip,port,target_url,he])
        except TooManyRedirects as te:
            self.return_list.append([ip,port,target_url,te])
        except Timeout as toe:
            self.return_list.append([ip,port,target_url,toe])
        finally:
            return self.return_list