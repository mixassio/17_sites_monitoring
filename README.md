# Sites Monitoring Utility

The script check url from your file url.txt and get answer about status server and date of expiry.
For work, create txt-file with list of url, for example:
- https://devman.org/
- https://habrahabr.ru/
- https://mail.ru/
- https://meduza.io/

# HOW RUN

Example of script launch on Linux, Python 3.6:

```#!bash

$ python check_sites_health.py 'puth-to-file-with-url.txt'
Site: https://devman.org/ Status server: 200 Date expiry: OK (End - 2017-08-28)
Site: https://habrahabr.ru/ Status server: 200 Date expiry: OK (End - 2018-04-18)
Site: https://mail.ru/ Status server: 200 Date expiry: OK (End - 2017-10-01)
Site: https://meduza.io/ Status server: 200 Date expiry: OK (End - 2017-07-21)
```

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
