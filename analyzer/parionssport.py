from bs4 import BeautifulSoup
import requests
import json

def make_parionssport_headers():
	headers = {
		'Host': 'www.enligne.parionssport.fdj.fr',
		'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0',
		'Accept': 'application/json, text/plain, */*',
		'Accept-Language': 'fr,fr-FR;q=0.8,en-US;q=0.5,en;q=0.3',
		# 'Accept-Encoding': 'gzip, deflate, br'
		'X-LVS-HSToken': 'try5Wy26j7p-RpzIndadeK6sD44bNIN5hPn45KCEoUO8InJ3RxRJnyCguxKLYfoTdxavWp4ufDDLfhZ6TKdHdUCwDDA5fve37Alw2nrxnWXqMvK6uuPvSQQZ2r0ssTS4y558LPb_ZhkEfgk1615D9w==',
		# 'Connection': 'keep-alive'
		'Referer': 'https://www.enligne.parionssport.fdj.fr/paris-football',
		'Sec-Fetch-Dest': 'empty',
		'Sec-Fetch-Mode': 'cors',
		'Sec-Fetch-Site': 'same-origin',
		'If-None-Match': 'W/"1816b-mOq4gHIct5ZQSa1k/cLfzXimqfQ"'
	}
	return headers

def get_parionssport_core(url):
	ret = []

	for page in range(1):
		r = requests.get(url % page, headers=make_parionssport_headers())
		data = json.loads(r.text)
		data = data['items']
		for it in data:
			try:
				names = []
				names.append(data[it]['a'].strip().lower())
				names.append(data[it]['b'].strip().lower())
				cotes = []
				for itt in data:
					if itt == it:
						continue
					try:
						print(f'{data[itt]["feedCode"]} == {data[it]["feedCode"]}')
						if data[itt]['feedCode'] == data[it]['feedCode']:
							print("dzeoifzein")
							cotes.append(data[itt]['price'])
					except:
						continue
			except:
				continue
			if len(names) > 0 and len(cotes) > 0:
				tmp = []
				tmp.append(names)
				tmp.append(cotes)
				ret.append(tmp)
	return ret

def get_parionssport_football():
    return get_parionssport_core('https://www.enligne.parionssport.fdj.fr/lvs-api/next/50/p240?lineId=1&originId=3&breakdownEventsIntoDays=true&showPromotions=true&pageIndex=%d')
def get_parionssport_baseball():
    return get_parionssport_core('https://www.enligne.parionssport.fdj.fr/paris-baseball')
def get_parionssport_tennis():
    return get_parionssport_core('https://www.enligne.parionssport.fdj.fr/paris-tennis')
def get_parionssport_handball():
    return get_parionssport_core('https://www.enligne.parionssport.fdj.fr/paris-handball')

parionssport = {
    'football': get_parionssport_football,
    'baseball': get_parionssport_baseball,
    'tennis':   get_parionssport_tennis,
    'handball': get_parionssport_handball
}

def get_parionssport(sport):
    if sport in parionssport:
        return parionssport[sport]()
    return []

r = get_parionssport('football')
print(r)
print(len(r))
