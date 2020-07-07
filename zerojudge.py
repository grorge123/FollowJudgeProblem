import requests
from bs4 import BeautifulSoup

url = "https://tioj.ck.tp.edu.tw/users/"
name = "grorge"

se = requests.session()
re = se.get(url + name)
soup = BeautifulSoup(re.text, 'html.parser')

tag = soup.find_all(class_="text-success")
url = 'https://tioj.ck.tp.edu.tw/problems/'


for i in tag:
	re = requests.get(url + i.text)
	soup = BeautifulSoup(re.text, 'html.parser')
	head = soup.find_all(class_="page-header")
	print(head[0].text, url + i.text)
print(len(tag))