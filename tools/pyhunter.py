#! /usr/bin/env python3

# [PyHunter ~ 0.1]
# Author: NateMount (@NateMount)

# === Imports

from sys import argv
from requests import Session, Response, RequestException
from random import choice

# === PyHunter Class
class PyHunter:

    USER_AGENTS = (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 Safari/605.1.15",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1",
        "Mozilla/5.0 (Linux; Android 11; SM-G991B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.105 Mobile Safari/537.36",
    )

    def __init__(self, url:str):
        self.log = lambda msg: None
        self.session = Session()
        self.headers = {
            "User-Agent": "PyHunter/0.2",
            "Accept": "*/*",
            "Connection": "keep-alive"
        }
        self.url = url

    def connect(self, url:str) -> Response:
        self.log(f"Attemtping connection to {url}")

        try:
            response:Response = self.session.get(url, headers=self.headers, timeout=10)
            if response.status_code not in (403, 429):
                self.log("Connection Established")
                return response
            
            self.log(f"Connection Blocked [{response.status_code}], Rotating User Agents...")
        except RequestException as err:
            self.log(f"Connection Error: {err}")
            pass

        for ua in self.USER_AGENTS:
            self.headers["User-Agent"] = ua
            try:
                self.log(f"New UA: {ua}")
                response = self.session.get(url, headers=self.headers, timeout=10)
                if response.status_code not in (403, 429):
                    self.log("Connection Established")
                    return response
            except RequestException as err:
                self.log(f"New UA Failed [{response.status_code}]")
                continue
        
        self.log("Failed to Connect With All Availible User-Agents")
        return None

    def analyse_verification_method(self, valid_user:str, invalid_user:str = "PH000XIP12") -> dict:

        valid_response:Response = self.connect(self.url.format(valid_user))
        if valid_response is None:
            return {'Error': 'Cannot Connect to Valid User Profile'}
        
        invalid_response:Response = self.connect(self.url.format(invalid_user))
        if invalid_response is None:
            return {'Error': 'Cannot Connect to InValid User Profile'}
        
        mapping:dict = {
            "headers": self.headers,
            "cookies": self.session.cookies.get_dict(),
            "check_type": None,
            "criteria": {}
        }

        method_found:bool = False

        if valid_response.status_code != invalid_response.status_code:
            mapping['check_type'] = 'status_code'
            mapping['criteria'] = {
                'valid': valid_response.status_code, 
                'invalid':invalid_response.status_code
            }
            self.log(f"Method Found: Status Code +[{valid_response.status_code}] VS -[{invalid_response.status_code}]")
            method_found = True
        
        if not method_found and valid_response.url.replace(valid_user, '@@@@@') != invalid_response.url.replace(invalid_user, '@@@@@'):
            mapping["check_type"] = 'url'
            mapping['criteria'] = {
                'valid': valid_response.url.replace(valid_user, '@@@@@'),
                'invalid': invalid_response.url.replace(invalid_user, '@@@@@')
            }
            method_found = True
        
        if not method_found and (valid_len := len(valid_response.text.replace(valid_user, '@@@@@'))) != (invalid_len := len(invalid_response.text.replace(invalid_user, '@@@@@'))):
            mapping['check_type'] = 'length'
            mapping['criteria'] = {
                'valid': valid_len,
                'invalid': invalid_len
            }
            method_found = True
        
        if not method_found and '404' in invalid_response.text:
            mapping['check_type'] = 'content'
            mapping['criteria'] = {
                'valid': '@@@Unknown@@@',
                'invalid': '404'
            }
        
        if method_found:
            if not self._test_cookies(valid_user, mapping):
                mapping['cookies'] = {}
            return mapping

        return {'Error': 'No Valid Method Found'}

    def _test_cookies(self, username:str, mapping:dict) -> bool:
        tmp_session = Session()

        try:
            response = tmp_session.get(self.url.format(username), headers=self.headers, timeout=10)
        except RequestException:
            return True
        
        match mapping['check_type']:
            case 'status_code':
                if response.status_code != mapping['criteria']['valid']:
                    self.log(f"Cookies Required, Status Code [{response.status_code}]")
                    return True
            
            case 'url':
                if response.url.replace(username, '@@@@@') != mapping['criteria']['valid']:
                    self.log(f"Cookies Required, URL [{response.url.replace(username, '@@@@@')}]")
                    return True
            
            case 'length':
                current_len:int = len(response.text)
                if abs(current_len - mapping['criteria']['valid']) > abs(current_len - mapping['criteria']['invalid']):
                    self.log(f"Cookies Required, Len [{current_len} is Closer to InValid Len than Valid Len]")
                    return True
        self.log("No Cookies Required")
        return False

# === Main Program 
def main() -> None:
    if len(argv) < 3:
        print("[PyHunter ~]:\n\nUsage:\n\tpython3 pyhunder.py <url> <valid_username> [/v]")
        return 
    
    # args[1] should be the provided URL
    hunter:PyHunter = PyHunter(argv[1])

    if '/v' in argv:
        hunter.log = lambda msg: print(f"[PyHunter::Info ~]: {msg}")
    
    # args[2] should be valid username
    print(hunter.analyse_verification_method(argv[2]))

if __name__ == '__main__':
    main()