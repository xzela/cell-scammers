import requests
import random
import names
import string
import sys
import time

url = 'http://sprint.restoretheaccount.info/login.php'
def post ():
    # fake the user agent for maximum results!
    headers = { 'User-Agent': 'Mozilla/5.0 (Windows NT 6.0; WOW64; rv:24.0) Gecko/20100101 Firefox/24.0' }
    # generate some random data so it looks real
    data = {
        'user': names.get_last_name(),
        'pass': ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(10)),
        'number': random.sample(xrange(1000000000, 9999999999), 1)[0],
        'billzip': random.sample(xrange(10000, 99999), 1)[0],
        'pin': random.sample(xrange(1000, 9999), 1)[0],
    }

    try:
        r = requests.post(url, headers=headers, data=data)
        # It looks like they 302 the URL to a 404'd sprint page but the 
        # initial post (with all of the user data) is sent to their servers
    except requests.exceptions.Timeout:
        # Maybe set up for a retry, or continue in a retry loop
        print e
    except requests.exceptions.RequestException as e:
        # catastrophic error. bail.
        print e
        sys.exit(1)
i = 0;
while True:
    post()
    # throttle yourself so they don't throttle you!
    time.sleep(3)
    i = i + 1
    print "i've posted %i junk records" % i
