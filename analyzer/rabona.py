import json
import requests

def make_rabona_headers():
	headers = {
	'Host': 'sb2frontend-altenar2.biahosted.com',
	'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0',
	'Accept': '*/*',
	'Accept-Language': 'fr,fr-FR;q=0.8,en-US;q=0.5,en;q=0.3',
	# 'Accept-Encoding': 'gzip, deflate, br'
	'Origin': 'https://rabona1.com',
	'Sec-Fetch-Dest': 'empty',
	'Sec-Fetch-Mode': 'cors',
	'Sec-Fetch-Site': 'cross-site',
	'Referer': 'https://rabona1.com/'
	# 'Connection': 'keep-alive'
	}
	return headers


def get_rabona_core(url):
	ret = []
	r = requests.get(url, headers=make_rabona_headers())
	data = json.loads(r.text)
	data = data['Result']['Items'][0]['Events']

	for i in range(len(data)):
		names = []
		for j in range(len(data[i]['Competitors'])):
			names.append(data[i]['Competitors'][j]['Name'].strip().lower())
		cotes = []
		for j in range(len(data[i]['Items'][0]['Items'])):
			cotes.append(data[i]['Items'][0]['Items'][j]['Price'])
		if len(names) > 0 and len(cotes) > 0:
			tmp = []
			tmp.append(names)
			tmp.append(cotes)
			ret.append(tmp)
	return ret

def get_rabona_football():
	return get_rabona_core('https://sb2frontend-altenar2.biahosted.com/api/Sportsbook/GetUpcoming?timezoneOffset=-120&langId=39&skinName=rabona&configId=12&culture=fr-FR&countryCode=FR&deviceType=Desktop&numformat=en&integration=rabona&sportId=66&showAllEvents=false&count=100')
def get_rabona_basketball():
	return get_rabona_core('https://sb2frontend-altenar2.biahosted.com/api/Sportsbook/GetUpcoming?timezoneOffset=-120&langId=39&skinName=rabona&configId=12&culture=fr-FR&countryCode=FR&deviceType=Desktop&numformat=en&integration=rabona&sportId=67&showAllEvents=false&count=100')
def get_rabona_tennis():
	return get_rabona_core('https://sb2frontend-altenar2.biahosted.com/api/Sportsbook/GetUpcoming?timezoneOffset=-120&langId=39&skinName=rabona&configId=12&culture=fr-FR&countryCode=FR&deviceType=Desktop&numformat=en&integration=rabona&sportId=68&showAllEvents=false&count=100')
def get_rabona_baseball():
	return get_rabona_core('https://sb2frontend-altenar2.biahosted.com/api/Sportsbook/GetUpcoming?timezoneOffset=-120&langId=39&skinName=rabona&configId=12&culture=fr-FR&countryCode=FR&deviceType=Desktop&numformat=en&integration=rabona&sportId=76&showAllEvents=false&count=100')
def get_rabona_volleyball():
	return get_rabona_core('https://sb2frontend-altenar2.biahosted.com/api/Sportsbook/GetUpcoming?timezoneOffset=-120&langId=39&skinName=rabona&configId=12&culture=fr-FR&countryCode=FR&deviceType=Desktop&numformat=en&integration=rabona&sportId=69&showAllEvents=false&count=100')

rabona = {
	'football':   get_rabona_football,
	'basketball': get_rabona_basketball,
	'tennis':     get_rabona_tennis,
	'baseball':   get_rabona_baseball,
	'volleyball': get_rabona_volleyball
}

def get_rabona(sport):
	if sport in rabona:
		return rabona[sport]()
	return []
