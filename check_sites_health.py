import os
import json
import whois
import codecs
import requests
import chardet

def load_urls4check(filepath):
    if os.path.exists(filepath):
        with open(filepath, 'rb') as file_text:
            char_type = chardet.detect(file_text.read())['encoding']
        with codecs.open(filepath, 'rb', encoding=char_type) as file_text:
            return file_text.read().split('\r\n')

def is_server_respond_with_200(url):
    url_info = requests.get(url)
    return url_info.status_code

def get_domain_expiration_date(domain_name):
    domain = requests.get('http://htmlweb.ru/analiz/api.php?whois&url=devman.org&json')
    print(dir(domain))
    #print(domain['whois'])
    j = domain.json()
    print(j['whois'])
    print(j['limit'])
    print(j['creation'])
    print(j['paid'])

if __name__ == '__main__':
    list_url = load_urls4check('./url.txt')
    l = [line.strip() for line in list_url]
    print(list_url)
    print(is_server_respond_with_200('https://devman.org/'))
    get_domain_expiration_date('google.com')