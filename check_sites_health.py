import os
import re
import sys
from datetime import datetime, timedelta
import requests


def load_urls4check(filepath):
    if os.path.exists(filepath):
        with open(filepath, 'r') as file_text:
            list_url = [line.strip() for line in file_text]
    return list_url


def is_server_respond_with_200(url):
    url_info = requests.get(url)
    return url_info.status_code


def get_domain_expiration_date(domain_name):
    url = 'http://htmlweb.ru/analiz/api.php?whois&url=' + domain_name + '&json'
    domain = requests.get(url)
    if domain.json()['paid'] == '01.01.1970':
        result = re.findall(r'xpiry\s\w*\:\s\w*(\d\d\d\d\-\d\d\-\d\d)', domain.json()['whois'])
        date_expiry = datetime.strptime(result[0], "%Y-%m-%d").date()
    else:
        date_expiry = datetime.strptime(domain.json()['paid'], "%d.%m.%Y").date()
    if (date_expiry - timedelta(days=30)) > datetime.date(datetime.now()):
        date_ok = 'OK'
    else:
        date_ok = 'less month'
    return date_expiry, date_ok

if __name__ == '__main__':
    list_url = load_urls4check(sys.argv[1])
    for site in list_url:
        status_code = is_server_respond_with_200(site)
        date_expiry, date_ok = get_domain_expiration_date(site)
        print('Site: {} Status server: {} Date expiry: {} (End - {})'.format(site, status_code, date_ok, date_expiry))