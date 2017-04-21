import os
import re
from datetime import datetime, timedelta
import codecs
import requests
import chardet

def load_urls4check(filepath):
    if os.path.exists(filepath):
        with open(filepath, 'rb') as file_text:
            char_type = chardet.detect(file_text.read())['encoding']
        with codecs.open(filepath, 'rb', encoding=char_type) as file_text:
            return file_text.read().split('\r\n')

"""def TEMP_load_file(filepath):
    with open(filepath, 'rb') as file_text:
        char_type = chardet.detect(file_text.read())['encoding']
    with codecs.open(filepath, 'rb', encoding=char_type) as file_text:
        result = re.findall(r'Expiry Date: (\d\d\d\d\-\d\d\-\d\d)', file_text.read())
    date_expiry = datetime.strptime( result[0], "%Y-%m-%d").date()
    if (date_expiry - timedelta(days=30)) > datetime.date(datetime.now()):
        date_ok = True
    else:
        date_ok = False
    print(date_ok, type(date_ok))
"""


def is_server_respond_with_200(url):
    url_info = requests.get(url)
    return url_info.status_code

def get_domain_expiration_date(domain_name):
    domain = requests.get('http://htmlweb.ru/analiz/api.php?whois&url=' + domain_name + '&json')
    print(domain.json()['limit'])
    if domain.json()['paid'] == '01.01.1970':
        result = re.findall(r'xpiry\s\w*\:\s\w*(\d\d\d\d\-\d\d\-\d\d)', domain.json()['whois'])
        date_expiry = datetime.strptime(result[0], "%Y-%m-%d").date()
    else:
        date_expiry = datetime.strptime(domain.json()['paid'], "%d-%m-%Y").date()
    if (date_expiry - timedelta(days=30)) > datetime.date(datetime.now()):
        date_ok = 'OK'
    else:
        date_ok = 'less month'
    return date_expiry, date_ok

if __name__ == '__main__':
    list_url = load_urls4check('./url.txt')
    for site in list_url:
        print(site)
        status_code = is_server_respond_with_200(site)
        date_expiry, date_ok = get_domain_expiration_date(site)
        print('Site: {}\n Status server: {}\n Date expiry: {} (End - {})'.format(site, status_code, date_ok, date_expiry))