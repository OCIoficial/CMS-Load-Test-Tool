import requests
import random
import sys

####### CONFIG DATA #######
BASE_URL = 'http://server.com/'
USERNAME = "username"
PASSWORD = "password"

PROBLEMNAMES = [
    'ataque',
]
##########################

filenames = ['memory.cpp', 'hello.cpp', 'forever.cpp', 'hello.java', 'for.java', 'forever.java']

if len(sys.argv) > 1:
    n = int(sys.argv[1])
else:
    n = 10

url_submit = BASE_URL + 'tasks/%s/submit'
url_login = BASE_URL+'login'


s = requests.Session()

data = {
    'username': USERNAME,
    'password': PASSWORD
}

r = s.post(url_login, data=data)
if r.status_code != 200 or "Failed to log in" in r.text:
    print 'login fail'
    exit(1)
else:
    print 'login successful'

for i in range(n):
    problemname = random.choice(PROBLEMNAMES)
    filename = random.choice(filenames)
    old_filename = filename
    if filename.split('.')[1] == 'java':
        with open("files/"+filename) as fp:
            string = fp.read()
            string = string % problemname
            with open('files/%s.java' % problemname, 'w') as fp_w:
                fp_w.write(string)
        filename = "%s.java"%problemname
    files = {"%s.%%l" % problemname : open("files/"+filename, 'rb')}
    r = s.post(url_submit % problemname, files=files)
    print i, r, problemname, old_filename


