import requests
import time
from bs4 import BeautifulSoup
import hashlib
import random


ran = str(int(random.random() * 1000000))
name = 'grorge'
name = input()
key = ''
secret = ''
sha = hashlib.sha512()
sha.update((ran + '/user.status?apiKey=' + key + '&count=100&from=1' \
			+ '&handle=' + name + '&time=' + str(int(time.time())) + '#' + secret \
			).encode('utf-8'))
apisig = ran + sha.hexdigest()
url = 'https://codeforces.com/api/user.status?handle=' + \
		name + '&from=1&count=100&apiKey=' + key \
		+ '&time=' + str(int(time.time())) \
			+ '&apiSig=' + apisig		
#以上是codeforceapikey使用方式
url = 'https://codeforces.com/api/user.status?handle=' + \
		name + '&from=1&count=1000000'

se = requests.session()

re = se.get(url)
js = re.json()
se = set()
for i in js['result']:
	if (i['verdict'] == "OK"):
		se.add((i['problem']['name'], i['contestId'], i['problem']['index']))
for i in se:
	print(i[0],'https://codeforces.com/contest/' + str(i[1]) + '/problem/' + str(i[2]))
print(len(se))