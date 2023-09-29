from bs4 import BeautifulSoup
import requests

def make_netbet_headers():
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

def get_netbet_core(url):
	ret = []
	r = requests.get(url, headers=make_netbet_headers())
	soup = BeautifulSoup(r.text, 'html.parser')
	for div in list(soup.find_all('div', {'class': 'nb-event comingevents'})):
		names = []
		for name_div in list(div.find_all('div', {'class': 'nb-match_actor'})):
			names.append(name_div.get_text().strip().lower())
		cotes = []
		for cotes_div in list(div.find_all('div', {'class': 'nb-odds_amount'})):
			cotes.append(cotes_div.get_text().strip().lower())

		if len(names) > 0 and len(cotes) > 0:
			tmp = []
			tmp.append(names)
			tmp.append(cotes)
			ret.append(tmp)
	return ret

def get_netbet_football():
	return get_netbet_core('https://www.netbet.fr/football?tab=a-venir')
def get_netbet_tennis():
	return get_netbet_core('https://www.netbet.fr/tennis?tab=a-venir')
def get_netbet_basketball():
	return get_netbet_core('https://www.netbet.fr/basketball?tab=a-venir')
def get_netbet_handball():
	return get_netbet_core('https://www.netbet.fr/handball?tab=a-venir')
def get_netbet_baseball():
	return get_netbet_core('https://www.netbet.fr/baseball?tab=a-venir')
def get_netbet_boxe():
	return get_netbet_core('https://www.netbet.fr/boxe?tab=a-venir')

netbet = {
	'football':   get_netbet_football,
	'tennis':     get_netbet_tennis,
	'basketball': get_netbet_basketball,
	'handball':   get_netbet_handball,
	'baseball':   get_netbet_baseball,
	'boxe':       get_netbet_boxe 
}

def get_netbet(sport):
	if sport in netbet:
		return netbet[sport]()
	return []
