from bs4 import BeautifulSoup
import requests
import re
import json

def get_betclic_core(url):
	ret = []
	r = requests.get(url)
	data = json.loads(r.text)

	for i in range(len(data['matches'])):
		names = []
		if len(data['matches'][i]['contestants']) < 1:
			continue
		names.append(data['matches'][i]['contestants'][0]['short_name'].strip().lower())
		names.append(data['matches'][i]['contestants'][1]['short_name'].strip().lower())

		if len(data['matches'][i]['grouped_markets']) < 1:
			continue
		cotes = []
		for j in range(len(data['matches'][i]['grouped_markets'][0]['markets'][0]['selections'])):
			cotes.append(data['matches'][i]['grouped_markets'][0]['markets'][0]['selections'][j][0]['odds'])
		tmp = []
		tmp.append(names)
		tmp.append(cotes)
		ret.append(tmp)
	return ret

def get_betclic_football():
	return get_betclic_core('https://offer.cdn.begmedia.com/api/pub/v4/sports/1?application=2&countrycode=fr&hasSwitchMtc=true&language=fr&limit=120&markettypeId=1365&offset=0&sitecode=frfr&sortBy=ByLiveRankingPreliveDate')
def get_betclic_baseball():
	return get_betclic_core('https://offer.cdn.begmedia.com/api/pub/v4/sports/20?application=2&countrycode=fr&hasSwitchMtc=true&language=fr&limit=120&markettypeId=1152&offset=0&sitecode=frfr&sortBy=ByLiveRankingPreliveDate')
def get_betclic_handball():
	return get_betclic_core('https://offer.cdn.begmedia.com/api/pub/v4/sports/9?application=2&countrycode=fr&hasSwitchMtc=true&language=fr&limit=120&markettypeId=1400&offset=0&sitecode=frfr&sortBy=ByLiveRankingPreliveDate')
def get_betclic_tennis():
	return get_betclic_core('https://offer.cdn.begmedia.com/api/pub/v4/sports/2?application=2&countrycode=fr&hasSwitchMtc=true&language=fr&limit=120&markettypeId=2013&offset=0&sitecode=frfr&sortBy=ByLiveRankingPreliveDate')

def get_betclic(sport):
	if sport == 'football':
		return get_betclic_football()
	elif sport == 'tennis':
		return get_betclic_tennis()
	elif sport == 'handball':
		return get_betclic_handball()
	elif sport == 'baseball':
		return get_betclic_baseball()
	return []
