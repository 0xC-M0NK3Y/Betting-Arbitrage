from bs4 import BeautifulSoup
import requests
from requests_html import HTMLSession

"""

NOT WORKING

"""

def make_bwin_headers():
	headers = {
	'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0',
	'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
	'Accept-Language': 'fr,fr-FR;q=0.8,en-US;q=0.5,en;q=0.3',
	#'Accept-Encoding': 'gzip, deflate, br'
	#'Connection': 'keep-alive'
	'Upgrade-Insecure-Requests': '1',
	'Sec-Fetch-Dest': 'document',
	'Sec-Fetch-Mode': 'navigate',
	'Sec-Fetch-Site': 'none',
	'Sec-Fetch-User': '?1',
	'Pragma': 'no-cache',
	'Cache-Control': 'no-cache'}
	return headers

def get_bwin_incoming_footbal():
	ret = []
	s = HTMLSession()
	r = s.get('https://sports.bwin.fr/fr/sports/football-4', headers=make_bwin_headers())
	#print(r.html)
	r.html.render()
	#print(r.text)
	#soup = BeautifulSoup(r.text, 'html.parser')
	#print(r.text)
	print(r.html.html)
	"""
	for msevent in list(r.html.find('ms-event', {'class': 'grid-event ms-active-highlight ng-star-inserted'})):
		names = []
		for div_names in list(msevent.find_all('div', {'class': 'participant'})):
			names.append(div_names.get_text().strip())

		cotes = []
		msoption = div.find('ms-option', {'class': 'grid-option-group grid-group ng-star-inserted'})
		for cotes_msfont in list(msoption.find_all('ms-font-resizer')):
			cotes.append(cotes_msfont.get_text().strip())

		tmp = []
		tmp.append(names)
		tmp.append(cotes)
		ret.append(tmp)
	"""
	return ret
