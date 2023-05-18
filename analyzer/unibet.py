from bs4 import BeautifulSoup
import requests
import re

"""

NOT WORKING

"""

def make_unibet_headers():
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

def get_unibet_incoming_footbal():
	ret = []
	s = requests.session()
	s.get('https://www.unibet.fr/', headers=make_unibet_headers())
	r = requests.get('https://www.unibet.fr/sport/football', headers=make_unibet_headers())
	soup = BeautifulSoup(r.text, 'html.parser')
	print(r.text)
	for div in list(soup.find('div', {'class': re.compile('ui-touchlink had-market inline-market calendar-event cell event_*')})):
		names = []
		names_div = div.find('div', {'class': 'cell-event'})
		span = names_div.find('span')
		tmp_names = span.get_text().split('-')
		names.append(tmp_names[0].strip)
		names.append(tmp_names[1].strip)

		cotes = []
		for cotes_span in list(div.find_all('span', {'class': 'ui-touchlink-needsclick price odd-price'})):
			cotes.append(cotes_span.get_text().strip())
		tmp = []
		tmp.append(names)
		tmp.append(cotes)
		ret.append(tmp)
	return ret
