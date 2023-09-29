from bs4 import BeautifulSoup
import requests

def make_casinozer_headers():
	headers = {}
	return headers

def get_casinozer_core(url):
	ret = []

	# r = request.get(url, headers=make_casinozer_headers())
	# soup = bs4(r.text, 'html.parser')
	# for ... in soup.find_all:
	# 	names = []
	#   for n in div.find_all('div', 'class': 'names')
	#   	names.append(n.get_text().strip().lower())
	#  cotes = []
	# . ...
	#  	tmp = []
	# 	tmp.append(names)
	#	tmp.append(cotes)
	#	ret.append(tmp)
	return ret

def get_casinozer_football():
	return get_casinozer_core('https://casinozer.bet/fr/sport?bt-path=%2Fschedule%3FscheduleSport%3Dsoccer-1')

casinozer = {
	'football':   get_casinozer_football,
}

def get_casinozer(sport):
	if sport in casinozer:
		return casinozer[sport]()
	return []

print(get_casinozer('football'))
